import os
source_folder = "C:/Users/ad/Downloads"
for root, dirs, files in os.walk(source_folder):
    # print(files)
    for file in files:
        if file.lower().endswith('.pdf'):
            print(os.path.join(root, file),'\n')
        else:
            pass    
    #            source_path = os.path.join(root, file)
    #         #    pdf_files.append(source_path)
    #            print(f"Found: {source_path}")