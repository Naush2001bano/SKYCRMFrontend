from django.shortcuts import render,redirect
from django.http import HttpResponse,StreamingHttpResponse
import requests
import json
from datetime import datetime
import requests
import zipfile
import io
# Create your views here.
link="http://127.0.0.1:8001"
def login(request):
    return render(request,'login/login.html')

def dashboard(request):
    return render(request,'dashboard/dashboard.html')


def livem(request):
    return render(request, 'rtm/rtm.html')

def search(request):
    return render(request,"search/search.html")

def upload_export(request):
    return render(request,'upload_export/upload_export.html')

def non_attempted(request):
    return render(request,"non_attempted/non_attempted.html")

def missedcall(request):
    return render(request,"missedcall/missedcall.html")

def connect_to_customer(request):
    return render(request,"connect_to_customer/connect_to_customer.html")

def cms(request):
    lead__id = request.GET.get('id')
    rendered = request.GET.get('render')
    progressive = request.GET.get('progressive')
    print(lead__id)
    post_data = {'lead__id': lead__id,'rendered':rendered,'progressive':progressive}

    csrf_token = request.COOKIES.get('csrftoken')
    api_url = f'{link}/cms_data'
    headers = {'X-CSRFToken': csrf_token}
    response = requests.post(api_url, data=post_data )
    response_data = response.json()
    print(type(response_data))
    data_response = response_data['data']
    # print(data_response, 'dataresponse')
    context = ''
    for i in data_response:
        i['contacted_dt'] = datetime.strptime(i['contacted_dt'], '%Y-%m-%dT%H:%M:%S.%f')
        context = {'id':i['id'],'name':i['name'],'mobile':i['mobile_no'],'address':i['address'],'state':i['state'],'pincode':i['pincode'],'email':i['email'],'co_name':i['co_name'],'co_mobile_no':i['co_mobile_no'],'lender_name':i['lender_name'],'merchant_name':i['merchant_name'],'agreement_id':i['agreement_id'],'agreement_no':i['agreement_no'],'due_date':i['due_date'],"nach_status":i['nach_status'],"bounced_reason":i['bounced_reason'],"advisor":i['advisor'],'amount':i['main_amount'],'first_emi_date':i['first_emi_date'],'caller_name':i['caller_name'],"sub_disposition":i['sub_disposition'],"contacted_dt":i['contacted_dt'],'remark':i['remark'],'render':i['render'],'last_dial':i['last_dial_no'],'unassigned':i['Unassigned'],'attemptedby':i['attempted_by']}
    return render(request,"cms/cms.html",context)



def inc_cms(request):
    print("INComing CMS")
    lead__id = request.GET.get('id')
    rendered = request.GET.get('render')
    progressive = request.GET.get('progressive')
    print(lead__id)
    post_data = {'lead__id': lead__id,'rendered':rendered,'progressive':progressive}

    csrf_token = request.COOKIES.get('csrftoken')
    api_url = f'{link}/cms_data'
    headers = {'X-CSRFToken': csrf_token}
    response = requests.post(api_url, data=post_data )
    response_data = response.json()
    print(type(response_data))
    data_response = response_data['data']
    # print(data_response, 'dataresponse')
    context = ''
    for i in data_response:
        i['contacted_dt'] = datetime.strptime(i['contacted_dt'], '%Y-%m-%dT%H:%M:%S.%f')
        context = {'id':i['id'],'name':i['name'],'mobile':i['mobile_no'],'address':i['address'],'state':i['state'],'pincode':i['pincode'],'email':i['email'],'co_name':i['co_name'],'co_mobile_no':i['co_mobile_no'],'lender_name':i['lender_name'],'merchant_name':i['merchant_name'],'agreement_id':i['agreement_id'],'agreement_no':i['agreement_no'],'due_date':i['due_date'],"nach_status":i['nach_status'],"bounced_reason":i['bounced_reason'],"advisor":i['advisor'],'amount':i['main_amount'],'first_emi_date':i['first_emi_date'],'caller_name':i['caller_name'],"sub_disposition":i['sub_disposition'],"contacted_dt":i['contacted_dt'],'remark':i['remark'],'render':i['render'],'last_dial':i['last_dial_no'],'unassigned':i['Unassigned'],'attemptedby':i['attempted_by']}
    return render(request,"incomming/incomming.html",context)

def reminder(request):
    return render(request,"reminder/reminder.html")

def recovery(request):
    return render(request,"recovery/recovery.html")

def quality(request):
    return render(request,"quality/quality.html")

def leadupdate(request):
    return render(request,'leadupdate/leadupdate.html')

def dnd(request):
    return render(request,"dnd/dnd.html")

def score_card(request,id):
    print(id,'iddd')
    post_data = {'id':id}
    csrf_token = request.COOKIES.get('csrftoken')
    api_url = 'http://127.0.0.1:8001/get_score'
    headers = {'X-CSRFToken': csrf_token}
    response = requests.post(api_url, data=post_data )
    response_data = response.json()
    # print(type(response_data))
    data_response = response_data['data']
    # print(data_response, 'dataresponse')
    context = {}
    for i in data_response:
        # print(i['id'],i['agent'],i['direction'],i['sub'],i['phone'],i['recordingfile'],i['contacted_dt'])
        context = {'id':i['id'],'agent':i['agent'],'direction':i['direction'],'sub':i['sub'],'phone':i['phone'],'recordingfile':i['recordingfile'],'contacted_dt':i['contacted_dt']}
        
    return render(request,"quality/score.html",context)




MAX_TOTAL_FILE_SIZE = 1 * 1024 * 1024 * 1024  # 1 GB in bytes

def bulk_download(request):
    if request.method == "POST":
        try:
            rec_link = request.POST.get("rec_link").split(',')
            print(rec_link, "hdsfgdfgd")
            
            total_file_size = 0
            
            # Collect data about files to be downloaded
            download_data = []
            
            wrong_url = []
            empty_url = []
            
            if rec_link != [""]:
                for url in rec_link:
                    if url.strip():
                        response = requests.get(f"http://{url.strip()}")
                        if response.status_code == 200:
                            # Extract the file name from the URL
                            filename = url.split('/')[-1]
                            file_size = len(response.content)
                            
                            # Check if the total file size exceeds the limit
                            if total_file_size + file_size <= MAX_TOTAL_FILE_SIZE:
                                # Update total file size
                                total_file_size += file_size
                                
                                # Add download data to the list
                                download_data.append({"filename": filename, "content": response.content})
                            else:
                                # File size exceeds the limit, return error message
                                return redirect('/filesize')
                        else:
                            wrong_url.append(url)
                    else:
                        empty_url.append(url)
                
                if wrong_url or empty_url:
                    print(empty_url, wrong_url, "detailsssssssssssssssssssss")
                
            if download_data:
                # Create an in-memory file-like object
                in_memory_zip = io.BytesIO()
                
                # Create the ZIP file
                with zipfile.ZipFile(in_memory_zip, 'w', compression=zipfile.ZIP_DEFLATED, compresslevel=9) as zip_file:
                    for data in download_data:
                        # Write the file content to the zip file
                        zip_file.writestr(data["filename"], data["content"])
                
                # Seek to the beginning of the in-memory file
                in_memory_zip.seek(0)
                
                # Create a streaming response with the ZIP file content
                response = StreamingHttpResponse(in_memory_zip, content_type='application/zip')
                response['Content-Disposition'] = 'attachment; filename="recordings_files.zip"'
                
                return response
            # else:
            #     return 'no file selected'
        
        except Exception as e:
            print(e, "error")
    
    return redirect("/quality")

def filesize(request):
    return render(request,'filesize.html')


def create_user(request):
    return render(request,'createuser/createuser.html')

def sms(request):
    return render(request,"sms/sms.html")

def lead_behaviour(request):
    return render(request,"teamoverall/leadbehaviour.html")

def ptp_status(request):
    return render(request,"teamoverall/ptp_status.html")

def paid_status(request):
    return render(request,"teamoverall/paid_status.html")

def dispo_status(request):
    return render(request,"teamoverall/dispo_status.html")




    