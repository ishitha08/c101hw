class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token

    def upload_file(self, file_from, file_to):
        "upload a file to Dropbox using API v2"
        
        dbx = dropbox.Dropbox(self.access_token)

        with open(file_from, 'rb') as f:
            dbx.files_upload(f.read(), file_to)

def main():
    access_token = 'BcVeMSFv9KAAAAAAAAAADyMXZDGx8wxuDd9pThdhR70lAuz3BFGOvWf7-UdBqpMl'
    transferData = TransferData(access_token)

    file_from = 'test.txt'
    file_to = '/test_dropbox/test.txt'  


    transferData.upload_file(file_from, file_to)

if __name__ == '__main__':
    main()

import dropbox

client = dropbox.client.DropboxClient(<access_token>)
print 'linked account: ', client.account_info()

f = open('working-draft.txt', 'rb')
response = client.put_file('/magnum-opus.txt', f)
print 'uploaded: ', response

folder_metadata = client.metadata('/')
print 'metadata: ', folder_metadata

f, metadata = client.get_file_and_metadata('/magnum-opus.txt')
out = open('magnum-opus.txt', 'wb')
out.write(f.read())
out.close()
print metadata