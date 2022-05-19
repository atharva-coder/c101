import dropbox

class TransferData:
    def __init__(self,access_token):
        self.access_token=access_token
    def upload_file(self,file_from,file_to):
        dbx=dropbox.Dropbox(self.access_token)
        f=open(file_from,'rb')
        dbx.files_upload(f.read(),file_to)
def main():
    access_token='sl.BH7QcWdUs_zTNPouhYmq2jpuCDKlmsOe3bSXfC-jj9ttZw7XTsCbVcxq-UoduA9sOMmeHqowfjCabhi7tusxIrKOCxRspNOS1N3vjD4re7YvytaMjlhtNMdZnuB9iWE4szsugBKfwYY'
    transferdata=TransferData(access_token)    
    file_from=input("enter the file to transfered: ")
    file_to=input("enter the dropbox path: ")
    transferdata.upload_file(file_from,file_to)
    print("file has been moved")
main()        
