"big frame"
def main():
    "bigframe"
    text1 = input()
    text2 = input()
    text3 = input()
    text4 = input()
    text5 = input()
    alltext = []
    alltext.extend([text1,text2,text3,text4,text5])
    alltextclean = [text.rstrip() for text in alltext]
    N = max(len(text) for text in alltextclean)
    print("*"*(N+4))
    for i in alltextclean:
        space = N - len(i)
        print(f'* {i}{" "*space} *')
    print("*"*(N+4))

main()
