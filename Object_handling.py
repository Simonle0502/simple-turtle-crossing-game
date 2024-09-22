from Object import Object

OBJECT_NUM = 10
SCREEN_WIDTH = 300
OBJECTS_SPACE = 100
class Objects():
    def __init__(self,objects_speed):
        self.objects_list = []
        self.object_num =OBJECT_NUM
        self.objects_setup()
        self.objects_speed = objects_speed  

    def object_distance_control(self):
            setup_status = False
            while setup_status== False:
                object = Object()
                for index in self.objects_list:
                    if object.distance(index) < OBJECTS_SPACE:
                        object = Object()
                        break
                else:
                    setup_status = True
            return object

    def objects_setup(self):
        for object in range(self.object_num):
            object = self.object_distance_control()
            self.objects_list.append(object)
    

    def draw_objects(self):
        for index in range(len(self.objects_list)):
            self.objects_list[index].draw_object()

        
    def move_objects(self):
        for index in range(len(self.objects_list)):
            self.objects_list[index].forward(self.objects_speed)
    
    def update_objects(self):
        for obj in self.objects_list:
            if obj.xcor() > 300 :
                obj.delete_object()
                self.objects_list.remove(obj)
                new_object = self.object_distance_control()
                self.objects_list.append(new_object)
    
    def update_speed(self,new_speed):
        self.objects_speed = new_speed
                



