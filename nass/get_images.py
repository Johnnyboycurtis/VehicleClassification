import os
import sys
import requests
sys.path.append('/home/jonathan/Documents/ImageNASS')
import pynass.imagerequests as ir
from tqdm import tqdm 


with open('Cases.txt', 'r') as myfile:
    CaseIDs = []
    for line in myfile:
        CaseIDs.append(line.strip())
        

requester = ir.CrashViewerImageRequest(CaseID = CaseIDs, directory='/home/jonathan/Pictures/NASS')
requester.CrashViewerURL()
case_images = requester.get_img_url(return_=True)
requester.request_images()
