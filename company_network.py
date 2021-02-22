
def greed(company_network , distance ):

    num_com = company_network[0]
    cable = company_network[1]

    cable_1 = 0
    cable_2 = 0
    min_list = []
    boo = True
    for z in rnage(cable):
        i = 0
        min = 10 ** 7
        while i < len(distance):

            j = 1
            while j < len(distance):

                min_test = abs(distance[j]-distance[i])

                if min_test < min:
                    min = min_test
                    distance.remove(distance[j])
                    distance.remove(distance[i])

                    break



                j +=1


            i +=1






if __name__ == '__main__':
    company_network = list(map(int, input().split()))
    distance = []
    for i in range(company_network[0]):
        distance.append(int(input()))
    distance.sort()
    greed(company_network,distance)