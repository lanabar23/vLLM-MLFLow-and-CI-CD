from transformers import AutoModelForCausalLM, AutoTokenizer
from vllm.engine.async_llm_engine import AsyncLLMEngine
from vllm.engine.arg_utils import AsyncEngineArgs
from flask import Flask, request, jsonify
from huggingface_hub import login
import vllm
import os 


load_dotenv()
hf_access_token = os.getenv('HF_READ')
login(token=hf_access_token)

model_name = 'facebook/opt-1.3b'

app = Flask(__name__)

# Load the model using vLLM
# model = vllm.LLM(model='path_to_your_model', tokenizer='tokenizer_name')
# generator = vllm.SamplingParams()

tokenizer = AutoTokenizer.from_pretrained(model-name,
                token=token,
                trust_remote_code=True
                )

if tokenizer.pad_token_id is None:
    tokenizer.pad_token_id = tokenizer.eos_token_id

model = AutoModelForCausalLM.from_pretrained(model-name).to("cpu")

engine_args = AsyncEngineArgs(model=model-name)
engine = AsyncLLMEngine(engine_args)



@app.route('/predict', methods=['POST'])
def predict():
    # Get input from client
    data = request.get_json(force=True)
    prompt = data['text']

    # Generate output using the loaded model
    outputs = engine.generate([prompt], sampling_params=generator)
    generated_text = outputs[0].outputs[0].text.strip()  # Extract first output

    return jsonify({'response': generated_text})

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)