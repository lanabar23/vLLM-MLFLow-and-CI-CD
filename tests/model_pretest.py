from transformers import AutoModelForCausalLM, AutoTokenizer
from huggingface_hub import login
from dotenv import load_dotenv  
from langfuse import Langfuse
import pandas as pd
import torch
import time
import os

import models_and_prompts 


load_dotenv()
public_key = os.getenv('LF_PUBKEY')
secret_key = os.getenv('LF_SECKEY')
token = os.getenv('HF_READ')

login(token=token)

client = Langfuse(
  public_key=public_key,
  secret_key=secret_key,
  host="https://api.langfuse.com"
)

run = client.new_run()
run.name("Выбор модели для fine-tuning")
run.start()

# Класс для загрузки и тестирования моделей
class ModelLoader():
    def __init__(self, model_name_or_path):
        self.model_name_or_path = model_name_or_path
        #self.token = token
        self.model, self.tokenizer = self.load_model()

    def load_model(self):
        try:
            # Загрузим модель и токенайзер
            model = AutoModelForCausalLM.from_pretrained(self.model_name_or_path)
            tokenizer = AutoTokenizer.from_pretrained(self.model_name_or_path)

            # Перемещаем модель на GPU, если доступна
            device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
            model.to(device)

            return model, tokenizer
        except Exception as e:
            print(f"Ошибка при загрузке модели {self.model_name_or_path}: {e}")
            raise

    def generate_response(self, prompt):
        """
        Генерация ответа на заданный промпт
        """
        inputs = self.tokenizer.encode(prompt, return_tensors="pt").to(next(self.model.parameters()).device)
        start_time = time.time()
        with torch.no_grad():
            outputs = self.model.generate(inputs, max_new_tokens=50)
        generated_text = self.tokenizer.decode(outputs[0], skip_special_tokens=True)
        latency = round(time.time() - start_time, 2)
        #print(f'"prompt": {prompt}, "response": {generated_text}, "latency": l{latency}')
        return {"prompt": prompt, "response": generated_text, "latency": latency}

# Список моделей и соответствующих категорий запросов
models = models_and_prompts.models
prompts = models_and_prompts.prompts

# Основная логика тестирования
results = {}
for model_name, details in models.items():
    print(model_name)
    loader = ModelLoader(details[0])
    category = details[1]
    results[model_name] = {'responses': [], 'avg_latency': None}
    total_latency = 0
    for prompt in prompts.get(category, []):
        response_data = loader.generate_response(prompt)
        results[model_name]['responses'].append(response_data)
        total_latency += response_data['latency']
    avg_latency = total_latency / len(results[model_name]['responses'])
    results[model_name]['avg_latency'] = f"{avg_latency:.2f}" if results[model_name]['responses'] else "N/A"
    run.log_metrics(results)

# Формирование итогового отчета
# df_results = pd.DataFrame({
#     'Model Name': list(results.keys()),
#     'Average Latency': [result['avg_latency'] for result in results.values()],
#     'Responses Count': [len(result['responses']) for result in results.values()]
# })

print(df_results)

# metrics = {"accuracy": 0.85, "loss": 0.2}
# run.log_metrics(metrics)

run.finish()

