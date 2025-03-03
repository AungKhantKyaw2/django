from django.shortcuts import render
from django.http import HttpResponse

# Use a pipeline as a high-level helper
from transformers import pipeline

pipe = pipeline("text-generation", model="Aung2024/gpt2-large-span-head-finetuned-squad2")

def home(request):
    if request.method == 'POST':
        input_text = request.POST.get('input_text')
        context_text = request.POST.get('context_text')
        full_text =f"Question: {input_text} Context: {context_text}"
        quest_ans = pipe(full_text)
        print (quest_ans)
        return render(request,'index.html',{'quest_ans': quest_ans, 'input_text': input_text, 'context_text': context_text})
    return render(request,'index.html')  
