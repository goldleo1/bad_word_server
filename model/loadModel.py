import torch
from transformers import AutoTokenizer, AutoModelForSequenceClassification

device = torch.device('cuda:0' if torch.cuda.is_available() else 'cpu')
print('device :', device)
MY_MODEL = r'D:\\WORKSPACE\\WORK\\first_model\\trainer10000'
model_light = AutoModelForSequenceClassification.from_pretrained(
    MY_MODEL)
use_auth_token = True
MODEL_NAME = "beomi/KcELECTRA-base"
tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)


def sentence_predict(sent):
    model_light.eval()

    tokenized_sent = tokenizer(
        sent,
        return_tensors="pt",
        max_length=128,
        padding=True,
        truncation=True,
        add_special_tokens=True
    )
    tokenized_sent.to(device)

    with torch.no_grad():
        outputs = model_light(
            input_ids=tokenized_sent["input_ids"],
            attention_mask=tokenized_sent["attention_mask"],
            token_type_ids=tokenized_sent["token_type_ids"]
        )
    logits = outputs[0]
    logits = logits.detach().cpu()  # gpu의 데이터를 cpu 메모리로 복사
    accuracy = logits
    result = logits.argmax(-1)

    if result == 0:
        result = " >> 비속어 포함 👿"
    elif result == 1:
        result = " >> 비속어 비포함 😀"
    return {'result': result, 'accuracy': accuracy}


def sentence_predict_api(sent):
    model_light.eval()

    tokenized_sent = tokenizer(
        sent,
        return_tensors="pt",
        max_length=128,
        padding=True,
        truncation=True,
        add_special_tokens=True
    )
    tokenized_sent.to(device)

    with torch.no_grad():
        outputs = model_light(
            input_ids=tokenized_sent["input_ids"],
            attention_mask=tokenized_sent["attention_mask"],
            token_type_ids=tokenized_sent["token_type_ids"]
        )

    logits = outputs[0]
    logits = logits.detach().cpu()  # gpu의 데이터를 cpu 메모리로 복사
    accuracy = logits
    result = logits.argmax(-1)

    if result == 0:
        result = "bad"
    elif result == 1:
        result = "good"
    return {'result': result, 'accuracy': accuracy}


if __name__ == '__main':
    while True:
        sentence = input("댓글을 입력해주세요 : ")
        if sentence == '0':
            break
        print(sentence_predict(sentence))
        print('\n')
