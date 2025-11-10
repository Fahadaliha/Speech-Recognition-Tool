from recognizer import transcribe_audio
print("Hello and welcome to speech recognition system")

while True: #looping the input process with input type
    print("\n Choose input mode: ")
    print("1. Speak in mic")
    print("2. Audio file a (.wav file please)")
    print("3. exit")

    choice=input("Enter you choice: ").strip()

    if not choice.isdigit():
        print("Please choose between 3 given options")
        continue
    choice = int(choice)

    if choice ==1: #transcribing from mic
        print("\n Starting live recording...")
        result= transcribe_audio(mode="mic")
        print(result) #transcribing from .wav audio file
    elif choice ==2:
        file_path=input("Enter path to your audio file: ").strip()
        result = transcribe_audio(mode='file',file_path=file_path)
        print(result)

    elif choice == 3:
        print("Exiting...Thank you!")
    else:
        print("Invalid choice. please choose correct option")