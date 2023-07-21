from OpenAI import aichat



if __name__ == '__main__':
    charter = aichat.charter()
    print(charter.chat("what is your name"))