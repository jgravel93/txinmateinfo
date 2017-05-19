import urllib.request
import time
import pandas as pd
import math
from bs4 import BeautifulSoup


def getInmateInfo(filepath, header=None, names=None, idfield=None, savepath=None):

    url='https://offender.tdcj.texas.gov/OffenderSearch/offenderDetail.action?sid='
    df=pd.read_csv(filepath,header=header,names=names)
    sids=df[idfield].tolist()
    sids=['%08d'% int(x) for x in df[idfield].tolist() if math.isnan(x)==False]
    inmates={}
    maxhxnum=0
    colnames=['SID Number',
     'TDCJ Number',
     'Name',
     'Race',
     'Gender',
     'DOB',
     'Maximum Sentence Date',
     'Current Facility',
     'Projected Release Date',
     'Parole Eligibility Date',
     'Offender Visitation Eligible',
     'Scheduled Release Date',
     'Scheduled Release Type',
     'Scheduled Release Location',]


    for e,s in enumerate(sids):
        time.sleep(1)
        r=urllib.request.urlopen(url+str(s))
        soup=BeautifulSoup(r, 'lxml')
        fields=soup.findAll('div',class_="basic_os_left_column")
        values=soup.findAll('div',class_="basic_os_right_column")
        fields=[x.get_text().rstrip().lstrip().replace(':','') for x in fields]
        values=[x.get_text().rstrip().lstrip() for x in values]

        fvs=list(zip(fields,values))
        values_hx=[x.get_text().rstrip().lstrip() for x in soup.table.findAll('tr')]
        inmates[e]={}
        for(f,v) in fvs:
            inmates[e][str(f)]=v
        fields_hx=[x for x in values_hx[0].split('\n')]
        values_hx2=[[y for y in x.split('\n')] for x in values_hx[1:]]
        hx={}
        for enu,fi in enumerate(fields_hx):
            for en, val in enumerate(values_hx2):
                label=str(fi)+'_%d'% en
                value=val[enu]
                hx[label]=value
                if en>=maxhxnum:
                    maxhxnum=en
        for key,vals in hx.items():
            inmates[e][key]=vals

    for n in range(0,maxhxnum):
        newcols=['Offense Date_%d' % n, 'Offense_%d' % n,'Sentence Date_%d' % n,'County_%d' % n,'Case No._%d' % n,'Sentence (YY-MM-DD)_%d' % n]
        for c in newcols:
            colnames.append(c)

    df2=pd.DataFrame.from_dict(inmates,orient="index")
    df2=df2[colnames]
    if savepath!=None:
        df2.to_csv(savepath, sep='  ')
    return df2
def getInmateInfoNum2(SID):
    if len(SID)<8:
        sid2='0'+str(SID)
    else:
        sid2=str(SID)

    url='https://offender.tdcj.texas.gov/OffenderSearch/offenderDetail.action?sid='+str(sid2)
    print(url)

def getInmateInfoNum(SID):
    if len(SID)<8:
        sid2='0'+str(SID)
    else:
        sid2=str(SID)

    url='https://offender.tdcj.texas.gov/OffenderSearch/offenderDetail.action?sid='+str(sid2)

    #df=pd.read_csv(filepath,header=header,names=names)
    #sids=df[idfield].tolist()
    #sids=['%08d'% int(x) for x in df[idfield].tolist() if math.isnan(x)==False]
    inmates={}
    maxhxnum=0
    colnames=['SID Number',
     'TDCJ Number',
     'Name',
     'Race',
     'Gender',
     'DOB',
     'Maximum Sentence Date',
     'Current Facility',
     'Projected Release Date',
     'Parole Eligibility Date',
     'Offender Visitation Eligible',
     'Scheduled Release Date',
     'Scheduled Release Type',
     'Scheduled Release Location',]

    
    time.sleep(1)
    r=urllib.request.urlopen(url)
    soup=BeautifulSoup(r, 'lxml')
    fields=soup.findAll('div',class_="basic_os_left_column")
    values=soup.findAll('div',class_="basic_os_right_column")
    fields=[x.get_text().rstrip().lstrip().replace(':','') for x in fields]
    values=[x.get_text().rstrip().lstrip() for x in values]

    fvs=list(zip(fields,values))
    values_hx=[x.get_text().rstrip().lstrip() for x in soup.table.findAll('tr')]
    inmates[0]={}
    for(f,v) in fvs:
        inmates[0][str(f)]=v
    fields_hx=[x for x in values_hx[0].split('\n')]
    values_hx2=[[y for y in x.split('\n')] for x in values_hx[1:]]
    hx={}
    for enu,fi in enumerate(fields_hx):
        for en, val in enumerate(values_hx2):
            label=str(fi)+'_%d'% en
            value=val[enu]
            hx[label]=value
            if en>=maxhxnum:
                maxhxnum=en
    for key,vals in hx.items():
        inmates[0][key]=vals

    for n in range(0,maxhxnum):
        newcols=['Offense Date_%d' % n, 'Offense_%d' % n,'Sentence Date_%d' % n,'County_%d' % n,'Case No._%d' % n,'Sentence (YY-MM-DD)_%d' % n]
        for c in newcols:
            colnames.append(c)

    df2=pd.DataFrame.from_dict(inmates,orient="index")
    df2=df2[colnames]
    return df2
def getInmateInfoList(df):

    url='https://offender.tdcj.texas.gov/OffenderSearch/offenderDetail.action?sid='
    
    sids=df['SID'].tolist()
    sids=['%08d'% int(x) for x in sids if math.isnan(x)==False]
    inmates={}
    maxhxnum=0
    colnames=['SID Number',
     'TDCJ Number',
     'Name',
     'Race',
     'Gender',
     'DOB',
     'Maximum Sentence Date',
     'Current Facility',
     'Projected Release Date',
     'Parole Eligibility Date',
     'Offender Visitation Eligible',
     'Scheduled Release Date',
     'Scheduled Release Type',
     'Scheduled Release Location',]


    for e,s in enumerate(sids):
        time.sleep(1)
        r=urllib.request.urlopen(url+str(s))
        soup=BeautifulSoup(r, 'lxml')
        fields=soup.findAll('div',class_="basic_os_left_column")
        values=soup.findAll('div',class_="basic_os_right_column")
        fields=[x.get_text().rstrip().lstrip().replace(':','') for x in fields]
        values=[x.get_text().rstrip().lstrip() for x in values]

        fvs=list(zip(fields,values))
        values_hx=[x.get_text().rstrip().lstrip() for x in soup.table.findAll('tr')]
        inmates[e]={}
        for(f,v) in fvs:
            inmates[e][str(f)]=v
        fields_hx=[x for x in values_hx[0].split('\n')]
        values_hx2=[[y for y in x.split('\n')] for x in values_hx[1:]]
        hx={}
        for enu,fi in enumerate(fields_hx):
            for en, val in enumerate(values_hx2):
                label=str(fi)+'_%d'% en
                value=val[enu]
                hx[label]=value
                if en>=maxhxnum:
                    maxhxnum=en
        for key,vals in hx.items():
            inmates[e][key]=vals

    for n in range(0,maxhxnum):
        newcols=['Offense Date_%d' % n, 'Offense_%d' % n,'Sentence Date_%d' % n,'County_%d' % n,'Case No._%d' % n,'Sentence (YY-MM-DD)_%d' % n]
        for c in newcols:
            colnames.append(c)

    df2=pd.DataFrame.from_dict(inmates,orient="index")
    df2=df2[colnames]
    
        
    return df2

