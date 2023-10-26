from . import views
from django.conf import settings
from django.urls import path
from django.conf.urls.static import static



urlpatterns = [
    path('',views.login,name="login"),
    path('login',views.login,name="login"),
    path('dashboard',views.dashboard,name="dashboard"),
    path('livem',views.livem,name="livem"),
    #search
    path('search/',views.search,name="search"),

    #nonattempted
    path('non_attempted',views.non_attempted,name="non_attempted"),

    #dataupload 
    path('upload_export',views.upload_export,name="upload_export"),

    #leadupdate
    path('leadupdate',views.leadupdate,name="leadupdate"),

    #dnd
    path('dnd',views.dnd,name="dnd"),

    #cms
    path('cms',views.cms,name='cms'),

    
    #incoming_cms
    path('inc_cms',views.inc_cms,name="inc_cms"),

    #reminder
    path('reminder',views.reminder,name='reminder'),

    #rechurn
    path('recovery',views.recovery,name="recovery"),

    #qualiy
    path("quality",views.quality,name="quality"),

    #score
    path("score_card/<int:id>",views.score_card,name="score_card"),

    #bulk download
    path("bulk_download",views.bulk_download,name="bulk_download"),
    path('filesize',views.filesize,name="filesize"),

    #missedCall
    path('missedcall',views.missedcall,name="missedcall"),

    #createuser
    path("create_user",views.create_user,name="create_user"),

    #sms
    path('sms',views.sms,name="sms"),
    path('lead_behaviour',views.lead_behaviour,name="lead_behaviour"),
    path('ptp_status',views.ptp_status,name="ptp_status"),
    path('paid_status',views.paid_status,name="paid_status"),
    path('dispo_status',views.dispo_status,name="dispo_status"),

    path('connect_to_customer',views.connect_to_customer,name="connect_to_customer"),



]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)