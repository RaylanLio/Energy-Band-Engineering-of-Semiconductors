# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import math
def FDintegral(eta,eps):
    # Use a breakpoint in the code line below to debug your script.
#    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
    if eta >= 0 or eps < 0:
        exit()
    else:
        t = 0
        sign = 1
        t_sum = math.exp(eta)
        fd_sum = t_sum
        while t_sum > eps:
            sign = -sign
            t = t+1
            t_sum = math.exp((t+1)*eta)/math.pow(t+1,1.5)
            fd_sum = fd_sum+sign*t_sum
        #print("n={}",t)
        return fd_sum*math.sqrt(math.pi)/2


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print("F({0}) = {1}".format(-1,FDintegral(-1,1e-19)))


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
