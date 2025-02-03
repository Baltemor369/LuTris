# task list :
# + settings => option pour faciliter le jeu : previsualisation, cadrillage, option "random color", modifier key 

import tkinter as tk, random, time,datetime as dt,threading as th

def empty_board(width:int,heigth:int):
    blackboard=[]
    line=[]
    for i in range(0,width):
        line.append("black") # =empty case
    for i in range(0,heigth):
        blackboard.append(line.copy())
    return blackboard

class Coord():
    def __init__(self,x=0,y=0) -> None:
        self.x=x
        self.y=y
    
    def set_x(self,x:int):
        self.x=x
    def set_y(self,y:int):
        self.y=y
    
    def get_x(self):
        return self.x
    def get_y(self):
        return self.y

    def display(self):
        print(f"({self.get_x()}:{self.get_y()})")

class Brick():
    def __init__(self,pos:Coord,type:str):
        self.pos_up=[Coord(0,0)] # list coord relative to the main/first case
        self.pos_right=[Coord(0,0)]
        self.pos_down=[Coord(0,0)]
        self.pos_left=[Coord(0,0)]
        self.pos=pos
        self.type=type
        self.rotation=0 #vertical True=horizontal
        
        match self.type:
            case 'I':
                self.color="cyan"
                self.pos_up.append(Coord(0,-1))
                self.pos_up.append(Coord(0,-2))
                self.pos_up.append(Coord(0,1))

                self.pos_left.append(Coord(-2,0))
                self.pos_left.append(Coord(-1,0))
                self.pos_left.append(Coord(1,0))

                self.pos_down.append(Coord(0,-1))
                self.pos_down.append(Coord(0,-2))
                self.pos_down.append(Coord(0,1))
                
                self.pos_right.append(Coord(-2,0))
                self.pos_right.append(Coord(-1,0))
                self.pos_right.append(Coord(1,0))

            case 'J':
                self.color="blue"
                self.pos_up.append(Coord(-1,0))
                self.pos_up.append(Coord(0,-1))
                self.pos_up.append(Coord(0,-2))
                
                self.pos_left.append(Coord(0,1) )
                self.pos_left.append(Coord(-1,0))
                self.pos_left.append(Coord(-2,0))
                
                self.pos_down.append(Coord(1,0))
                self.pos_down.append(Coord(0,1))
                self.pos_down.append(Coord(0,2))
                
                self.pos_right.append(Coord(0,-1))
                self.pos_right.append(Coord(1,0))
                self.pos_right.append(Coord(2,0))
                
            case 'L':
                self.color="orange"
                self.pos_up.append(Coord(1,0))
                self.pos_up.append(Coord(0,-1))
                self.pos_up.append(Coord(0,-2))
                
                self.pos_left.append(Coord(0,-1))
                self.pos_left.append(Coord(-1,0))
                self.pos_left.append(Coord(-2,0))
                
                self.pos_down.append(Coord(-1,0 ))
                self.pos_down.append(Coord(0,1 ))
                self.pos_down.append(Coord(0,2 ))
                
                self.pos_right.append(Coord(0,1))
                self.pos_right.append(Coord(1,0))
                self.pos_right.append(Coord(2,0))      
                
            case 'S':
                self.color="green"
                self.pos_up.append(Coord(-1,0))
                self.pos_up.append(Coord(0,-1))
                self.pos_up.append(Coord(1,-1))
                
                self.pos_left.append(Coord(0,1))
                self.pos_left.append(Coord(-1,0))
                self.pos_left.append(Coord(-1,-1))
                
                self.pos_down.append(Coord(-1,0))
                self.pos_down.append(Coord(0,-1))
                self.pos_down.append(Coord(1,-1))
                
                self.pos_right.append(Coord(0,1))
                self.pos_right.append(Coord(-1,0))
                self.pos_right.append(Coord(-1,-1))
                
            case 'T':
                self.color="purple"
                self.pos_up.append(Coord(-1,0))
                self.pos_up.append(Coord(1,0))
                self.pos_up.append(Coord(0,-1))
                
                self.pos_left.append(Coord(-1,0 ))
                self.pos_left.append(Coord(0,1 ))
                self.pos_left.append(Coord(0,-1 ))
                
                self.pos_down.append(Coord(-1,0 ))
                self.pos_down.append(Coord(1,0 ))
                self.pos_down.append(Coord(0,1 ))
                
                self.pos_right.append(Coord(1,0))
                self.pos_right.append(Coord(0,-1))
                self.pos_right.append(Coord(0,1))
                
            case 'Z':
                self.color="red"
                self.pos_up.append(Coord(1,0))
                self.pos_up.append(Coord(0,-1))
                self.pos_up.append(Coord(-1,-1))
                
                self.pos_left.append(Coord(0,1))
                self.pos_left.append(Coord(1,0))
                self.pos_left.append(Coord(1,-1))
                
                self.pos_down.append(Coord(1,0))
                self.pos_down.append(Coord(0,-1))
                self.pos_down.append(Coord(-1,-1))
                
                self.pos_right.append(Coord(0,1))
                self.pos_right.append(Coord(1,0))
                self.pos_right.append(Coord(1,-1))

            case 'O':
                self.color="yellow"
                self.pos_up.append(Coord(1,0))
                self.pos_up.append(Coord(1,1))
                self.pos_up.append(Coord(0,1))
                
                self.pos_left.append(Coord(1,0))
                self.pos_left.append(Coord(1,1))
                self.pos_left.append(Coord(0,1))
                
                self.pos_down.append(Coord(1,0))
                self.pos_down.append(Coord(1,1))
                self.pos_down.append(Coord(0,1))
                
                self.pos_right.append(Coord(1,0))
                self.pos_right.append(Coord(1,1))
                self.pos_right.append(Coord(0,1))
                
    def set_x(self,x:int,ind:int):
        self.get_location()[ind].set_x(x)
    def set_y(self,y:int,ind:int):
        self.get_location()[ind].set_y(y)
    def set_rota(self,dir=0):
        self.rotation=dir
    
    def get_x(self,index:int):
        match self.get_rota():
            case 0:
                return self.pos_up[index].get_x()
            case 1:
                return self.pos_right[index].get_x()
            case 2:
                return self.pos_down[index].get_x()
            case 3:
                return self.pos_left[index].get_x()

    def get_y(self,index:int):
        match self.get_rota():
            case 0:
                return self.pos_up[index].get_y()
            case 1:
                return self.pos_right[index].get_y()
            case 2:
                return self.pos_down[index].get_y()
            case 3:
                return self.pos_left[index].get_y()

    def get_Position(self) :
        return self.pos

    def get_pos_list(self):
        match self.get_rota():
            case 0:
                return self.pos_up
            case 1:
                return self.pos_right
            case 2:
                return self.pos_down
            case 3:
                return self.pos_left

    def get_location(self):
        buff=[self.pos]
        for elt in self.get_pos_list():
            buff.append(Coord(self.get_Position().get_x()+elt.get_x() ,self.get_Position().get_y()+elt.get_y()))
        return buff

    def get_type(self):
        return self.type
    def get_color(self):
        return self.color
    def get_rota(self):
        return self.rotation
    
    def display(self):
        for elt in self.get_location():
            elt.display()
        print("end")

class Board():
    def __init__(self, width:int, height:int):
        self.buff_brick=""
        self.w=width
        self.h=height
        self.blackboard=empty_board(width,height)
        self.score=0

    def add_brick(self,brick : Brick):
        self.buff_brick=brick
        self.add_to_board(self.get_brick())
    
    def rmv_brick(self):
        self.buff_brick=""

    def move_right(self,event):
        self.erase_from_board(self.get_brick())

        check=True
        for elt in self.get_brick().get_location():
            if  elt.get_x() >= self.w:
                check=False
        if check:
                if self.collide(self.get_brick()).find("R")== -1:
                    for elt in self.get_brick().get_location():
                        elt.set_x(elt.get_x()+1)
        
        self.add_to_board(self.get_brick())

    def move_left(self,event):
        self.erase_from_board(self.get_brick())

        check=True
        for elt in self.get_brick().get_location():
            if  elt.get_x() <= 0:
                check=False
        if check:
            if self.collide(self.get_brick()).find("L")== -1:
                for elt in self.get_brick().get_location():
                    elt.set_x(elt.get_x()-1)
        

        self.add_to_board(self.get_brick())

    def move_down(self):
        self.erase_from_board(self.get_brick())
        
        #if not outside and no "Down" collision detected 
        if not self.out(self.get_brick()) and self.collide(self.get_brick()).find("D")== -1:
            for elt in self.get_brick().get_location():
                elt.set_y(elt.get_y()+1)
            self.add_to_board(self.get_brick())
        else:
            self.add_to_board(self.get_brick())
            self.rmv_brick()

    def add_to_board(self,brick:Brick):
        if brick!="":
            for elt in brick.get_location():
                if elt.get_y()>=0 and elt.get_y()<self.h:
                    self.set_case(Coord(elt.get_x(),elt.get_y()),brick.get_color())
    
    def erase_from_board(self,brick:Brick):
        if brick!="":
            for elt in brick.get_location():
                if elt.get_y()>=0 and elt.get_y()<self.h:
                    self.unset_case(Coord(elt.get_x(),elt.get_y()))

    def set_case(self,coord:Coord,value:str):
        self.blackboard[coord.get_y()][coord.get_x()]=value
    
    def set_line(self,y:int,line:list):
        self.blackboard[y]=line.copy()
        
    def unset_case(self,coord:Coord):
        self.blackboard[coord.get_y()][coord.get_x()]="black"
    
    def get_case(self,coord:Coord):
        return self.blackboard[coord.get_y()][coord.get_x()]

    def get_line(self,y:int):
        return self.blackboard[y] 
    
    def get_score(self):
        return self.score

    def get_brick(self):
        return self.buff_brick
                
    def del_line(self,y:int):
        for x in range(0,len(self.get_line(y))):
            self.unset_case(Coord(x,y))
        
    def is_empty(self,pos:Coord):
        if pos.get_x()<0 or pos.get_x()>= self.w or pos.get_y()>=self.h:
            return False
        return self.get_case(Coord(pos.get_x(),pos.get_y()))=="black"

    def collide(self,brick:Brick):
        not_empty=""
        for elt in brick.get_location():
            if elt.get_y()>=0:
                if not self.is_empty(Coord(elt.get_x(),elt.get_y()+1)):
                    not_empty+="D"
                if not self.is_empty(Coord(elt.get_x()+1,elt.get_y())):
                    not_empty+="R"
                if not self.is_empty(Coord(elt.get_x()-1,elt.get_y())):
                    not_empty+="L"
                if not self.is_empty(Coord(elt.get_x(),elt.get_y())):
                    not_empty+="I"
        return not_empty

    def out(self,brick:Brick):
        for elt in brick.get_location():
            if elt.get_y()>=self.h-1:
                return True
        return False
    
    def speed_down(self,event):
        if self.get_brick()!="":
            self.erase_from_board(self.get_brick())
            for elt in self.get_brick().get_location():
                if elt.get_y()<self.h and self.collide(self.get_brick()).find("D") == -1:
                    elt.set_y(elt.get_y()+1)
            self.add_to_board(self.get_brick())

    def rotate_R(self,event):
        self.erase_from_board(self.get_brick())
        self.get_brick().set_rota((self.get_brick().get_rota()+1)%4)
        tmp=False
        for elt in self.get_brick().get_location():
            if elt.get_x()<0 or elt.get_x()>=self.w or elt.get_y()>=self.h:
                tmp=True
        if self.collide(self.get_brick()).find("I")!= -1 or tmp:
            self.get_brick().set_rota((self.get_brick().get_rota()-1)%4)
        self.add_to_board(self.get_brick())

    def rotate_L(self,event):
        self.erase_from_board(self.get_brick())
        self.get_brick().set_rota((self.get_brick().get_rota()-1)%4)
        tmp=False
        for elt in self.get_brick().get_location():
            if elt.get_x()<0 or elt.get_x()>=self.w or elt.get_y()>=self.h:
                tmp=True
        if self.collide(self.get_brick()).find("I")!=-1 or tmp:
            self.get_brick().set_rota((self.get_brick().get_rota()+1)%4)
        self.add_to_board(self.get_brick())

    def check_full_line(self):
        delta=0
        for y in range(0,len(self.blackboard)):
            full_line=True
            for x in range(0,len(self.get_line(y))):
                if self.is_empty(Coord(x,y)):
                    full_line=False
            if full_line:
                delta+=1
                self.del_line(y)
                for i in range(y,1,-1):
                    self.set_line(i,self.get_line(i-1))
                self.score+=100*delta

    def display(self):
        for line in self.blackboard:
            print(line)
        print("\n")

class Tetris(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.title="Tetris"
        self.window_width=500
        self.window_height=800
        self.x=(self.winfo_screenwidth()-self.window_width)/2
        self.y=(self.winfo_screenheight()-self.window_height)/2
        self.geometry(f"{self.window_width}x{self.window_height}+{int(self.x)}+{int(self.y)}")

        self.pseudo=""
        self.tab=""
        self.file_name="data.txt"
        self.canva_bg="black"
        self.canva_width=11 # nb column
        self.canva_height=25 # nb row
        self.brick_size=20 #px size
        self.grid=False
        self.preview_fall=False
        self.random_color=False        
        
    def run(self):
        self.dis_menu()
    
    def clear_data(self):
        self.file=open("data.txt","w")
        self.file.write("")
        self.file.close()
        self.dis_show_score()

    def game(self):
        self.endgame=0
        self.time=1
        self.score=0
        self.board=Board(self.canva_width,self.canva_height)
        self.bind("<a>",self.board.rotate_L)
        self.bind("<e>",self.board.rotate_R)
        self.bind("<Right>",self.board.move_right)
        self.bind("<Left>",self.board.move_left)
        self.bind("<Down>",self.board.speed_down)
        self.dis_game()
        self.loop()

    def loop(self):
        type=["J","I","L","S","T","Z","O"]
        random.shuffle(type)
        if self.board.get_brick()=="":
            self.board.check_full_line()
            self.board.add_brick(Brick(Coord(int(self.canva_width/2),0) , type[random.randrange(0,len(type)*100)//100]))
        if moveBrick.is_set():
            self.board.move_down()
            moveBrick.clear()
        self.score=self.board.get_score()
        self.dis_loop()
        self.check_loose()
        self.time+=1
        if self.endgame==0:
            self.after(1,self.loop)
        if self.endgame==1:
            self.dis_score()

    def save_score(self):
        self.pseudo=self.nick_E.get()
        if self.pseudo!="":
            data = str(dt.datetime.today().month)+"-"+str(dt.datetime.today().day)+"-"+str(dt.datetime.today().year)+" "+str(dt.datetime.today().hour)+":"+str(dt.datetime.today().minute)+":"+str(dt.datetime.today().second)+" : "+self.pseudo+" : "+str(self.score)+"\n"
            self.file=open(self.file_name,"a")
            self.file.write(data)
            self.file.close()
        self.dis_menu()

    def show_score(self):
        self.file=open(self.file_name,"r")
        self.data=self.file.read()
        self.file.close()
        self.dis_show_score()
    
    def check_loose(self):
        self.board.erase_from_board(self.board.get_brick())
        for x in range(0,len(self.board.get_line(1))):
            if not self.board.is_empty(Coord(x,1)):
                self.endgame=1
        self.board.add_to_board(self.board.get_brick())

    def clear(self):
        if self.tab=="menu":
            self.clear_menu()
        if self.tab=="game":
            self.endgame=2
            self.clear_game()
        if self.tab=="score":
            self.clear_score()
        if self.tab=="setting":
            self.clear_setting()
        if self.tab=="show_score":
            self.clear_show_score()

    def dis_menu(self):
        self.clear()
        self.tab="menu"

        self.start_b=tk.Button(self,text="New Game",command=self.game,width=10)
        self.show_score_b=tk.Button(self,text="Show score",command=self.show_score,width=10)
        # self.settings_b=tk.Button(self,text="Settings",command=self.dis_setting,width=10)
        self.return_B=tk.Button(self,text="Return",command=self.dis_menu,width=10)
        self.exit_b=tk.Button(self,text="Exit",command=self.destroy,width=10)

        self.start_b.pack(pady=10)
        self.show_score_b.pack(pady=10)
        # self.settings_b.pack(pady=10)
        self.exit_b.pack(pady=10)
    
    def dis_game(self):
        self.clear()
        self.tab="game"

        self.score_L=tk.Label(self,text=self.score)
        self.canva=tk.Canvas(self,width=self.canva_width*self.brick_size,height=self.canva_height*self.brick_size,bg=self.canva_bg)
        self.score_L.pack()
        self.canva.pack()
        self.return_B.pack(pady=5)
    
    def dis_loop(self):
        self.score_L.config(text=self.score)
        self.canva.delete("all")
        for line in range(0,len(self.board.blackboard)):
            for case in range(0,len(self.board.get_line(line))):
                if not self.board.is_empty(Coord(case,line)) :
                    self.canva.create_rectangle(case*self.brick_size, line*self.brick_size, case*self.brick_size+self.brick_size, line*self.brick_size+self.brick_size, fill=self.board.get_case(Coord(case,line)))

    def dis_score(self):
        self.clear()
        self.tab="score"

        self.label=tk.Label(self,text="Enter a nickname to save your score : ")
        self.nick_E=tk.Entry(self,width=20)
        self.score_B=tk.Button(self,text="Register",command=self.save_score)

        self.label.pack()
        self.nick_E.pack()
        self.score_B.pack()
        self.return_B.pack(pady=5)
    
    def dis_show_score(self):
        self.clear()
        self.tab="show_score"

        self.label=tk.Label(self,text=self.data)
        self.clear_data_B=tk.Button(self,text="Clear",command=self.clear_data)

        self.label.pack()
        self.clear_data_B.pack()
        self.return_B.pack(pady=5)

    def dis_setting(self):
        self.clear()
        self.tab="setting"

        self.return_B.pack(pady=5)

    def clear_menu(self):
        self.start_b.pack_forget()
        self.show_score_b.pack_forget()
        # self.settings_b.pack_forget()
        self.exit_b.pack_forget()
    
    def clear_game(self):
        self.score_L.pack_forget()
        self.canva.pack_forget()
        self.return_B.pack_forget()

    def clear_score(self):
        self.label.pack_forget()
        self.nick_E.pack_forget()
        self.score_B.pack_forget()
        self.return_B.pack_forget()

    def clear_show_score(self):
        self.label.pack_forget()
        self.clear_data_B.pack_forget()
        self.return_B.pack_forget()

    def clear_setting(self):
        self.return_B.pack_forget()

class Clock(th.Thread):
    def __init__(self):
        th.Thread.__init__(self)
        self.stop=True

    def run(self):
        while self.stop:
            time.sleep(1/(5))
            moveBrick.set()

    def exit(self):
        self.stop=False

class Game(th.Thread):
    def __init__(self):
        th.Thread.__init__(self)
        self.tetris=Tetris()
        self.clock=Clock()
    def run(self):
        self.tetris.run()
        self.clock.start()
        

moveBrick=th.Event()

game=Game()
game.start()
game.tetris.mainloop()
game.clock.exit()
game._stop()
