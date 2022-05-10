#TODO

def doLongformer(txt):
	input_ids = torch.tensor(tokenizer_long.encode(txt)).unsqueeze(0)  # batch of size 1

	# TVM code doesn't work on CPU. Uncomment this if `config.attention_mode = 'tvm'`
	# model = model.cuda(); input_ids = input_ids.cuda()

	# Attention mask values -- 0: no attention, 1: local attention, 2: global attention
	attention_mask = torch.ones(input_ids.shape, dtype=torch.long, device=input_ids.device) # initialize to local attention
	attention_mask[:, [1, 4, 21,]] =  2  # Set global attention based on the task. For example,
										# classification: the <s> token
										# QA: question tokens

	output = model_long(input_ids, attention_mask=attention_mask)[0]
	return output