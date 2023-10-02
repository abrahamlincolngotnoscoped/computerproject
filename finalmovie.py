import tkinter as tk
import tkinter.messagebox
from tkinter import ttk
import mysql.connector

# Database connection parameters
db_params = {
    "host": "localhost",  # Replace with your MySQL host
    "user": "root",  # Replace with your MySQL username
    "password": "1234",  # Replace with your MySQL password
    "database": "movies"  # The name of your MySQL database
}

db_connection = mysql.connector.connect(**db_params)

class MovieApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Movie Ticket Booking System")
        self.root.geometry("1280x720")
        self.root.config(bg="darkblue")

        text_color = "black"
        entry_bg_color = "lightblue"

        self.Movie_Name = tk.StringVar()
        self.Movie_ID = tk.StringVar()
        self.Release_Date = tk.StringVar()
        self.Director = tk.StringVar()
        self.Cast = tk.StringVar()
        self.Budget = tk.StringVar()
        self.Duration = tk.StringVar()
        self.Rating = tk.StringVar()

        def iExit():
            iExit = tk.messagebox.askyesno("Movie Ticket Booking System", "Are you sure???")
            if iExit > 0:
                root.destroy()
            return

        def clcdata():
            self.txtMovie_ID.delete(0, tk.END)
            self.txtMovie_Name.delete(0, tk.END)
            self.txtRelease_Date.delete(0, tk.END)
            self.txtDirector.delete(0, tk.END)
            self.txtCast.delete(0, tk.END)
            self.txtBudget.delete(0, tk.END)
            self.txtRating.delete(0, tk.END)
            self.txtDuration.delete(0, tk.END)

        def adddata():
            if len(self.Movie_ID.get()) != 0:
                cursor = db_connection.cursor()
                query = "INSERT INTO MovieInfo (MovieID, MovieName, ReleaseDate, Director, Cast, Budget, Duration, Rating) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
                data = (self.Movie_ID.get(), self.Movie_Name.get(), self.Release_Date.get(),
                        self.Director.get(), self.Cast.get(), self.Budget.get(),
                        self.Duration.get(), self.Rating.get())
                cursor.execute(query, data)
                db_connection.commit()
                cursor.close()
                MovieList.delete(0, tk.END)
                MovieList.insert(tk.END, data)

        def disdata():
            
            MovieList.delete(0, tk.END)
            
            cursor = db_connection.cursor()
            cursor.execute("SELECT * FROM MovieInfo")
            
            for row in cursor.fetchall():
                
                MovieList.insert(tk.END, row)
            
            cursor.close()


        def movierec(event):
            global sd
            searchmovie = MovieList.curselection()[0]
            sd = MovieList.get(searchmovie)

            self.txtMovie_ID.delete(0, tk.END)
            self.txtMovie_ID.insert(tk.END, sd[1])
            self.txtMovie_Name.delete(0, tk.END)
            self.txtMovie_Name.insert(tk.END, sd[2])
            self.txtRelease_Date.delete(0, tk.END)
            self.txtRelease_Date.insert(tk.END, sd[3])
            self.txtDirector.delete(0, tk.END)
            self.txtDirector.insert(tk.END, sd[4])
            self.txtCast.delete(0, tk.END)
            self.txtCast.insert(tk.END, sd[5])
            self.txtBudget.delete(0, tk.END)
            self.txtBudget.insert(tk.END, sd[6])
            self.txtDuration.delete(0, tk.END)
            self.txtDuration.insert(tk.END, sd[7])
            self.txtRating.delete(0, tk.END)
            self.txtRating.insert(tk.END, sd[8])

        def deldata():
            if len(self.Movie_ID.get()) != 0:
                cursor = db_connection.cursor()
                cursor.execute("DELETE FROM MovieInfo WHERE ID = %s", (sd[0],))
                db_connection.commit()
                cursor.close()
                clcdata()
                disdata()

        def searchdb():
            MovieList.delete(0, tk.END)
            cursor = db_connection.cursor()
            
            # Get the values entered by the user in the entry fields
            movie_id = self.Movie_ID.get()
            movie_name = self.Movie_Name.get()

            # Define the query condition based on user input
            query_condition = ""
            query_values = ()
            
            if movie_id:
                query_condition += "MovieID = %s AND "
                query_values += (movie_id,)
            
            if movie_name:
                query_condition += "MovieName = %s AND "
                query_values += (movie_name,)
            
            # Remove the trailing "AND" if it exists
            if query_condition.endswith("AND "):
                query_condition = query_condition[:-4]
            
            query = f"SELECT * FROM MovieInfo WHERE {query_condition}"
            
            cursor.execute(query, query_values)
            
            for row in cursor.fetchall():
                MovieList.insert(tk.END, row)
            
            cursor.close()


        def updata():
            if len(self.Movie_ID.get()) != 0:
                cursor = db_connection.cursor()
                cursor.execute("DELETE FROM MovieInfo WHERE ID = %s", (sd[0],))
                query = "INSERT INTO MovieInfo (MovieID, MovieName, ReleaseDate, Director, Cast, Budget, Duration, Rating) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
                data = (self.Movie_ID.get(), self.Movie_Name.get(), self.Release_Date.get(),
                        self.Director.get(), self.Cast.get(), self.Budget.get(),
                        self.Duration.get(), self.Rating.get())
                cursor.execute(query, data)
                db_connection.commit()
                cursor.close()
                MovieList.delete(0, tk.END)
                MovieList.insert(tk.END, data)

        MainFrame = tk.Frame(self.root, bg="darkblue")
        MainFrame.grid()

        TFrame = tk.Frame(MainFrame, bd=5, padx=54, pady=8, bg="darkblue", relief=tk.RIDGE)
        TFrame.pack(side=tk.TOP)

        self.TFrame = tk.Label(TFrame, font=('Arial', 36, 'bold'),
                               text="MOVIE TICKET BOOKING SYSTEM", bg="darkblue", fg="white")
        self.TFrame.grid()

        BFrame = tk.Frame(MainFrame, bd=2, width=1280, height=70, padx=18, pady=10, bg="darkblue", relief=tk.RIDGE)
        BFrame.pack(side=tk.BOTTOM)

        DFrame = tk.Frame(MainFrame, bd=2, width=1240, height=400, padx=20, pady=20, bg="darkblue", relief=tk.RIDGE)
        DFrame.pack(side=tk.BOTTOM)

        DFrameL = tk.LabelFrame(DFrame, bd=2, width=1000, height=600, padx=20, bg="darkblue", relief=tk.RIDGE,
                               font=('Arial', 20, 'bold'), text="Movie Info_\n", fg="black")
        DFrameL.pack(side=tk.LEFT)

        DFrameR = tk.LabelFrame(DFrame, bd=2, width=450, height=300, padx=31, pady=3, bg="darkblue", relief=tk.RIDGE,
                               font=('Arial', 20, 'bold'), text="Movie Details\n", fg="black")
        DFrameR.pack(side=tk.RIGHT)

        self.lblMovie_ID = tk.Label(DFrameL, font=('Arial', 18, 'bold'), text="Movie ID:", padx=2, pady=2,
                                    bg="darkblue", fg="black")
        self.lblMovie_ID.grid(row=0, column=0, sticky=tk.W)
        self.txtMovie_ID = tk.Entry(DFrameL, font=('Arial', 18, 'bold'), textvariable=self.Movie_ID, width=29,
                                    bg=entry_bg_color, fg=text_color)
        self.txtMovie_ID.grid(row=0, column=1, padx=10, pady=10)

        self.lblMovie_Name = tk.Label(DFrameL, font=('Arial', 18, 'bold'), text="Movie Name:", padx=2, pady=2,
                                      bg="darkblue", fg="black")
        self.lblMovie_Name.grid(row=1, column=0, sticky=tk.W)
        self.txtMovie_Name = tk.Entry(DFrameL, font=('Arial', 18, 'bold'), textvariable=self.Movie_Name, width=29,
                                      bg=entry_bg_color, fg=text_color)
        self.txtMovie_Name.grid(row=1, column=1, padx=10, pady=10)

        self.lblRelease_Date = tk.Label(DFrameL, font=('Arial', 18, 'bold'), text="Release Date:", padx=2, pady=2,
                                        bg="darkblue", fg="black")
        self.lblRelease_Date.grid(row=2, column=0, sticky=tk.W)
        self.txtRelease_Date = tk.Entry(DFrameL, font=('Arial', 18, 'bold'), textvariable=self.Release_Date, width=29,
                                        bg=entry_bg_color, fg=text_color)
        self.txtRelease_Date.grid(row=2, column=1, padx=10, pady=10)

        self.lblDirector = tk.Label(DFrameL, font=('Arial', 18, 'bold'), text="Director:", padx=2, pady=2,
                                    bg="darkblue", fg="black")
        self.lblDirector.grid(row=3, column=0, sticky=tk.W)
        self.txtDirector = tk.Entry(DFrameL, font=('Arial', 18, 'bold'), textvariable=self.Director, width=29,
                                    bg=entry_bg_color, fg=text_color)
        self.txtDirector.grid(row=3, column=1, padx=10, pady=10)

        self.lblCast = tk.Label(DFrameL, font=('Arial', 18, 'bold'), text="Cast:", padx=2, pady=2, bg="darkblue",
                                fg="black")
        self.lblCast.grid(row=4, column=0, sticky=tk.W)
        self.txtCast = tk.Entry(DFrameL, font=('Arial', 18, 'bold'), textvariable=self.Cast, width=29,
                                bg=entry_bg_color, fg=text_color)
        self.txtCast.grid(row=4, column=1, padx=10, pady=10)

        self.lblBudget = tk.Label(DFrameL, font=('Arial', 18, 'bold'), text="Budget (Crores INR):", padx=2, pady=2,
                                  bg="darkblue", fg="black")
        self.lblBudget.grid(row=5, column=0, sticky=tk.W)
        self.txtBudget = tk.Entry(DFrameL, font=('Arial', 18, 'bold'), textvariable=self.Budget, width=29,
                                  bg=entry_bg_color, fg=text_color)
        self.txtBudget.grid(row=5, column=1, padx=10, pady=10)

        self.lblDuration = tk.Label(DFrameL, font=('Arial', 18, 'bold'), text="Duration (Hrs):", padx=2, pady=2,
                                    bg="darkblue", fg="black")
        self.lblDuration.grid(row=6, column=0, sticky=tk.W)
        self.txtDuration = tk.Entry(DFrameL, font=('Arial', 18, 'bold'), textvariable=self.Duration, width=29,
                                    bg=entry_bg_color, fg=text_color)
        self.txtDuration.grid(row=6, column=1, padx=10, pady=10)

        self.lblRating = tk.Label(DFrameL, font=('Arial', 18, 'bold'), text="Rating (Out of 5):", padx=2, pady=2,
                                  bg="darkblue", fg="black")
        self.lblRating.grid(row=7, column=0, sticky=tk.W)
        self.txtRating = tk.Entry(DFrameL, font=('Arial', 18, 'bold'), textvariable=self.Rating, width=29,
                                  bg=entry_bg_color, fg=text_color)
        self.txtRating.grid(row=7, column=1, padx=10, pady=10)

        sb = tk.Scrollbar(DFrameR)
        sb.grid(row=0, column=1, sticky='ns')

        MovieList = tk.Listbox(DFrameR, width=29, height=16, font=('Arial', 12, 'bold'), bg=entry_bg_color,
                               fg=text_color, yscrollcommand=sb.set)
        MovieList.bind('<<ListboxSelect>>', movierec)
        MovieList.grid(row=0, column=0, padx=8)
        sb.config(command=MovieList.yview)

        self.btnadd = tk.Button(BFrame, text="Add New", font=('Arial', 20, 'bold'), width=10, height=1, bd=4,
                                bg="white", command=adddata)
        self.btnadd.grid(row=0, column=0)

        self.btndis = tk.Button(BFrame, text="Display", font=('Arial', 20, 'bold'), width=10, height=1, bd=4,
                                bg="white", command=disdata)
        self.btndis.grid(row=0, column=1)

        self.btnclc = tk.Button(BFrame, text="Clear", font=('Arial', 20, 'bold'), width=10, height=1, bd=4,
                                bg="white", command=clcdata)
        self.btnclc.grid(row=0, column=2)

        self.btnse = tk.Button(BFrame, text="Search", font=('Arial', 20, 'bold'), width=10, height=1, bd=4,
                               bg="white", command=searchdb)
        self.btnse.grid(row=0, column=3)

        self.btndel = tk.Button(BFrame, text="Delete", font=('Arial', 20, 'bold'), width=10, height=1, bd=4,
                                bg="white", command=deldata)
        self.btndel.grid(row=0, column=4)

        self.btnup = tk.Button(BFrame, text="Update", font=('Arial', 20, 'bold'), width=10, height=1, bd=4,
                               bg="white", command=updata)
        self.btnup.grid(row=0, column=5)

        self.btnx = tk.Button(BFrame, text="Exit", font=('Arial', 20, 'bold'), width=10, height=1, bd=4, bg="white",
                             command=iExit)
        self.btnx.grid(row=0, column=6)


if __name__ == '__main__':
    root = tk.Tk()
    datbase = MovieApp(root)
    root.mainloop()
