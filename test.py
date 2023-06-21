from transformers import AutoTokenizer, M2M100ForConditionalGeneration
import torch
model = M2M100ForConditionalGeneration.from_pretrained("facebook/m2m100_418M").to(torch.device("cuda:0"))
tokenizer = AutoTokenizer.from_pretrained("facebook/m2m100_418M")

text_to_translate = "Life is like a box of chocolates"
model_inputs = tokenizer(text_to_translate, return_tensors="pt").to(torch.device("cuda:0"))
gen_tokens = model.generate(**model_inputs, forced_bos_token_id=tokenizer.get_lang_id("ja"), max_new_tokens=1000)
print(tokenizer.batch_decode(gen_tokens, skip_special_tokens=True)[0])
