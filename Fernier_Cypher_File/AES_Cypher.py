import base64
from cryptography.fernet import Fernet
import argparse

#argument section
parser = argparse.ArgumentParser()
parser.add_argument('-Encrypt', help='Give the file to encrypt', type=str)
parser.add_argument('-Decrypt', help='Give the file to Decrypt', type=str)
parser.add_argument('-Key', help='Give the fernel key', type=str)
parser.add_argument('-o', help='Give the output of the file that you whant to encrypt', type=str)
args = parser.parse_args()


def encypt_file():
    put_key = bytes(str(args.Key),'UTF-8')
    put_key = base64.b64encode(put_key)
    f = Fernet(put_key)
    
    with open(args.Encrypt ,"r") as enc:
        with open(args.o,"w") as enc_file:
            enc_lines = enc.readlines()
            for enc_line in enc_lines:
                byte_line_encrypt = bytes(str(enc_line),'UTF-8')
                encrypt = f.encrypt(byte_line_encrypt)
                enc_file.write(encrypt.decode('UTF-8'))
                enc_file.write("\n")
                
def decrypt_file():
    put_key = bytes(str(args.Key),'UTF-8')
    put_key = base64.b64encode(put_key)
    f = Fernet(put_key)
    with open(args.Decrypt,"r") as enc:
        dec_lines = enc.readlines()
        for dec_line in dec_lines: 
            byte_line_decrypt = bytes(str(dec_line),'UTF-8')
            decrypt = f.decrypt(byte_line_decrypt)
            print(decrypt.decode('UTF-8'))


if __name__ == "__main__": 
    if args.Encrypt: 
        encypt_file()
    if args.Decrypt: 
        decrypt_file()
    