# Project
__We are required to build one QNA LLM for our Vels university.__

# LLM used:
We use TinyLlama LLM which has below given properties:
* It has __1.1 Billion__ parameters.
* It has __3 trillion__ tokens.
* It has been trained on __16 A100-40G GPUs__
* It can be deployed in hardware with restricted memory access and computational capacities.

# Technique used:
I have fine-tuned the TinyLlama LLM to our custom dataset [__dataset.json__]. We have used free Google Collab T4 GPU to fine-tune the model. We have also used various techniques like 8-bit quantizer [using bitsandbytes module]. We have ran __250 steps__ with nearly __35 epochs__ to fine-tune [really less but that's what I could do with the free Google Collab T4 GPU].

# Model Response:
Here are few responses of the model:<br>
![Why Vels University](/images/special_about_vels_RESPONSE.png)<br>
![Location of Vels University](/images/location_RESPONSE.png)<br>
![Infrastruce of Vels University](/images/infrastructure_RESPONSE.png)<br>
![Courses Provided](/images/courses_provided_RESPONSE.png)<br>
<br>
You can see other Responses of the model in /images directory.

# Hugging Face Link:
If you wanna try this then check out: https://huggingface.co/ClaudeRitchie/tinyllama-vels-v1 This is the fine-tuned model.

# Future Outline:
* Fine-tune Llama2 instead of Tinyllama [or better go with Llama3]
* Try a larger dataset with atleast 10000 examples
* Run on a larger GPU like A100 to train the model.
* Train it for more epochs
* Keep the max_token to a higher number instead of a mere 100.

# Opensource Projects used:
* TinyLlama: https://github.com/jzhang38/TinyLlama

### Thank You ;)    