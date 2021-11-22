
n=20
i=1
while(i<=5):
    guess=int(input("guess the no"))

    if (guess > n):
        print("greater than real no")

    elif (guess < n):
        print("smaller than no")

    elif (guess == n):
        print("boom you are correct")
        break
    else:
        print("enter validate no")

    print("no of guesses left",5-i)

    i=i+1


if(guess>5 or guess==n):
    print("game over")



