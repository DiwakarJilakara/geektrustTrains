from constants import Constant
from combinetrains import MergeTrains
class TrainJourney1:
    def get_trains_information(self,train_a_input,train_b_input):
        train_a_input=self.get_train_status(train_a_input)
        train_b_input=self.get_train_status(train_b_input)
        merage_trains=MergeTrains()
        train_ab_output=merage_trains.get_train_after_combining(train_a_input,train_b_input) #self.train_after_combining(train_a_input,train_b_input)
        return [train_a_input,train_b_input,train_ab_output]

    def get_train_status(self,train_input):
        train_input1=[]
        for station in train_input:
            if station in Constant.train_a_information.keys():
                if Constant.train_a_information[station]>Constant.train_a_meeting_station_distance:
                    train_input1.append(station)
            elif station in Constant.train_b_information.keys():
                if Constant.train_b_information[station] > Constant.train_b_meeting_station_distance:
                    train_input1.append(station) 
        return train_input1

