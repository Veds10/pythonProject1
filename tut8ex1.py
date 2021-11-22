try:
      d1 = {"beam": "to smile",
            "furious": "angry",
            "starving": "hungry",
            "small": "tiny"}

      print("which word do you want to find")
      d2 = input()
      print(d1[d2])

except Exception as e:
      print("enter valid word",e)
