import os
import shutil

folder_path = r"C:\Users\vindh\OneDrive\Desktop\ishan\suu_birthday"
file_types = {
    "Images": [".jpg", ".jpeg", ".png", ".gif"],
    "Documents": [".doc", ".docx", ".txt"],
    "PDFs": [".pdf"],
    "Videos": [".mp4", ".mkv"],
    "Audio": [".mp3", ".wav"]
}
organized_count = 0
for file in os.listdir(folder_path):
    file_path = os.path.join(folder_path, file)
    if os.path.isfile(file_path):
        extension = os.path.splitext(file)[1].lower()
    for category , extensions  in file_types.items():
      if extension in extensions:
          target_folder = os.path.join(folder_path,category)
          os.makedirs(
              target_folder,
              exist_ok = True
          )
          destination_path = os.path.join(target_folder,file)
          try:
          
            shutil.move(
                file_path,
                destination_path
            ) 
            organized_count += 1
            print(
                    f"{file} moved to {category}"
                )
            
          except Exception as e:
              print(
                    f"Error moving {file}: {e}"
                )
          break
print("completed")