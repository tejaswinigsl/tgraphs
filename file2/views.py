from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.views.generic import View
from rest_framework.views import APIView
from rest_framework.response import Response
import pandas as pd 
import numpy as np 

# Create your views here.
'''class HomeView(View):
    def get(self,request,*args,**kwargs):
        return render(request,'charts.html',{"customers":10})
def home(request,*args,**kwargs):
    data={
        'sales':100,
        'customers':10,
    }
    return JsonResponse(data)

class ChartData(APIView):
   
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
        data={
                'sales':100,
                'customers':10,
                }
        return Response(data)'''


def homepage(request):
	return render(request,'charts.html')

class GraphData(APIView):
    def get(self,request,format=None):
        y=['male','female']
        x=[592,551]
        df=pd.read_csv(r"C:\Users\HP\Desktop\cloudearl\data\KAG_conversion_data.csv")
        x=df.iloc[:,6]
        a=df.iloc[:,4].value_counts()
        data1=df.iloc[:,4:6]
        b=df.iloc[:,7]
        
        df1=df.sort_values(by=['Impressions','Spent'],ascending=True)
        x1=df1.iloc[:,6]
        y1=df1.iloc[:,8]
        y2=df1.iloc[:,7]
        #x=data.iloc[[:,4],[:,5]].groupby('gender').agg(['mean'])
        x=data1.groupby('gender').count()
        xyz_count=df.iloc[:,1].value_counts()
        xyz_label=df.iloc[:,1].unique()
        #xyz_label=[916,936,1178]
        s=df.groupby(['xyz_campaign_id','gender']).size()
        female_count_id=s.iloc[::2].values
        male_count_id=s.iloc[1::2].values
        ageSum = df.groupby(by=['age']).sum()
        ageSum.drop(['ad_id', 'fb_campaign_id'], axis=1, inplace=True)
        ageConvRate = ageSum['Approved_Conversion']/ageSum['Clicks']*100
        age_label=df.iloc[:,3].unique()
        f=df.groupby(['age','xyz_campaign_id']).size()
        id1_count=f.iloc[:3]
        id2_count=f.iloc[3:6]
        id3_count=f.iloc[6:]

        
        data = {"labels":y,"DefaultData":a}
        data1= {"labels1":x1,"DefaultData1":y1}
        data2={"label2":x1,"DefaultData2":y2}
        data3={"labels3":xyz_label,"DefaultData3":xyz_count}
        data4={"DefaultData41":female_count_id,"DefaultData42":male_count_id}
        data5={'labels5':age_label,"DefaultData5":ageConvRate}
        data6={'DefaultData61':id1_count,'DefaultData62':id2_count,'DefaultData63':id3_count}
        graphs=[data,data1,data2,data3,data4,data5,data6]
        
      
        return Response(graphs)