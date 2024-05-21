def countChar(S):
    letterCount = 0
    numberCount = 0
    specialCount = 0

    alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    numbers = ['1','2','3','4','5','6','7','8','9','0']

    for char in S:
        if char.isupper():
            char = char.lower()

        if char in alphabet:
            letterCount += 1

        elif char in numbers:
            numberCount += 1

        else:
            specialCount += 1

    print("Letter count =", letterCount, "Digit count =", numberCount, "Special character count =", specialCount)

countChar("3 beautiful days.")
