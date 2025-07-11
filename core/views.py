from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse, HttpResponse
from .logic.extract import extract_text_from_pdf, generate_medical_chronology
from .logic.pneumonia_detector import detect_pneumonia_local

import os

UPLOAD_FOLDER = "core/uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

def upload_form(request):
    return render(request, "upload.html")

def index(request):
    return render(request, 'index.html')

def chatbot(request):
    return render(request, 'chatbot.html')


@csrf_exempt
def upload_file(request):
    if request.method == "POST":
        file = request.FILES.get("pdf")
        if not file:
            return HttpResponse("No file uploaded", status=400)

        file_path = os.path.join(UPLOAD_FOLDER, file.name)
        with open(file_path, "wb+") as destination:
            for chunk in file.chunks():
                destination.write(chunk)

        text = extract_text_from_pdf(file_path)
        chronology = generate_medical_chronology(text)

        return render(request, "result.html", {"summary": chronology})

    return HttpResponse("Method Not Allowed", status=405)

@csrf_exempt
def download_json(request):
    if request.method == "POST":
        summary = request.POST.get("summary", "")
        response = HttpResponse(summary, content_type="application/json")
        response["Content-Disposition"] = 'attachment; filename="summary.json"'
        return response
    return HttpResponse("Method Not Allowed", status=405)

# ----------------------------
# ✅ PNEUMONIA DETECTION VIEWS
# ----------------------------

def pneumonia_page(request):
    return render(request, "pneumonia-upload.html")  # Will be created in Step 4

@csrf_exempt
def upload_xray(request):
    if request.method == "POST":
        image = request.FILES.get("xray")
        if not image:
            return HttpResponse("No image uploaded", status=400)

        file_path = os.path.join(UPLOAD_FOLDER, image.name)
        with open(file_path, "wb+") as destination:
            for chunk in image.chunks():
                destination.write(chunk)

        result = detect_pneumonia_local(file_path)  

        os.remove(file_path)
        return render(request, "pneumonia-result.html", {"result": result})