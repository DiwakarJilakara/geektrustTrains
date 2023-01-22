from constants import Constant
class MergeTrains:
    def get_train_after_combining(self,train1,train2):
        train_a=[]
        train_b=[]
        train_ab=[]
        for station in train1:
            if station in Constant.train_a_information.keys():
                train_a.append((Constant.train_a_information[station]-Constant.train_a_information['hyb']))
            elif station in Constant.train_b_information.keys():
                 train_b.append((Constant.train_b_information[station]-Constant.train_b_information['hyb']))

        
        for station in train2:
            if station in Constant.train_a_information.keys():
                train_a.append((Constant.train_a_information[station]-Constant.train_a_information['hyb']))
            elif station in Constant.train_b_information.keys():
                train_b.append((Constant.train_b_information[station]-Constant.train_b_information['hyb']))

        train_b.sort(reverse=True) 
        train_a.sort(reverse=True)
        train_a_distances=list(Constant.train_a_information.values())
        train_b_distances=list(Constant.train_b_information.values())
        train_a_stations=list(Constant.train_a_information.keys())
        train_b_stations=list(Constant.train_b_information.keys())
        return self.combine_trains(train1, train2, train_a, train_b, train_ab, train_a_distances, train_b_distances, train_a_stations, train_b_stations)

    def combine_trains(self, train1, train2, train_a, train_b, train_ab, train_a_distances, train_b_distances, train_a_stations, train_b_stations):
        while(len(train1)!=0 or len(train2)!=0):
            if(len(train_a)==0 or len(train_b)==0):
                if(len(train_a)==0):
                    while(len(train_b)!=0):
                        train_ab.append(train_b_stations[train_b_distances.index(train_b[0]+Constant.train_b_information['hyb'])])
                        train_b.remove(train_b[0])
                    break
                elif(len(train_b)==0):
                    while(len(train_a)!=0):
                        train_ab.append(train_a_stations[train_a_distances.index(train_a[0]+Constant.train_a_information['hyb'])])
                        train_a.remove(train_a[0])
                    break
                else:
                    break
            if(train_b[0]>train_a[0]):
                  train_ab.append(train_a_stations[train_a_distances.index(train_a[0]+Constant.train_a_meeting_station_distance)])
                  train_a.remove(train_a[0])
             
            elif(train_b[0]<train_a[0]):
                train_ab.append(train_b_stations[train_b_distances.index(train_b[0]+Constant.train_b_meeting_station_distance)])
                train_b.remove(train_b[0])
        return train_ab

