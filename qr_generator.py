import tkinter as tk;
from tkinter import ttk;
from tkinter import messagebox as mb
from PIL import ImageTk, Image;
import os;
import qrcode;
#
#	In this class, we create a view for our application 
#	where the user will enter the data that the qr code will contain.
#
#	Author: Edgard Díaz
#


class view:

	def genera_code(self,frame,SSID,Seguridad, Password,Visibilidad):

		if SSID != "" and Password != "":
			
			if Visibilidad == "Si":
			
				Visibilidad = "true";
			else:
				Visibilidad = "false";

			qr = qrcode.QRCode(
			 version = 1,
			 error_correction = qrcode.constants.ERROR_CORRECT_Q, #About 35% or less errors can be corrected.
			 box_size = 6,
			 border = 2,
			)
			qr.add_data('WIFI:T:'+Seguridad+';S:'+SSID+';P:'+Password+';H:'+Visibilidad+';'); #Url or information that will contain the qr code.
			qr.make(fit = True);
			
			img = qr.make_image(fill_color = "black", black_color = "black");

			
			output = open("output2.png", "wb");
			img.save(output);

			self.QR_Show(frame)

			output.close();

		else:
			mb.showerror("Cuidado","Llene todos los campos");

	def QR_Show(self,f):
		
		self.canvas = tk.Canvas(f, width = 280, height = 280, bg = "white");
		self.canvas.place(x = 7, y = 10);
		self.img = tk.PhotoImage(file="output2.png");
		self.canvas.create_image(140,140, image = self.img);
		

	def ViewGenerateQR(self):
		
		ventana  = tk.Tk();
		ventana.resizable(0,0);
		ventana.title("QR Generator 1.0")
		
		#Frame que contendra el codigo QR generado
		f = tk.Frame(ventana, bg  = "white", bd = 1, width = 300, height = 300);
		f.grid(row=0, column=0, sticky ="NW");
		f.grid_propagate(0)
		f.update()
		

		#Frame que contiene  los campos requeridos para generar el QR
		f2 = tk.Frame(ventana, bd = 1, width = 300, height = 150);
		f2.grid(row=1, column=0, sticky ="NW");
		f2.grid_propagate(0)
		f2.update()

		#componentes del Frame 2

		lblSSID = tk.Label(f2, text = "SSID: ", font =("Verdana",12));
		lblSSID.place(x = 42 ,y = 15, anchor = "center");
		txtSSID = tk.Entry(f2);
		txtSSID.place(x = 120, y = 0, width=145);
		
		
		lblSeg = tk.Label(f2, text = "Seguridad:", font =("verdana", 12));
		lblSeg.place(x = 60, y = 40, anchor ="center");
		cbxSeg = ttk.Combobox(f2,state="readonly",values=["Ninguna","WPA","WEP"])
		cbxSeg.current(1)
		cbxSeg.place(x = 120, y = 25);


		lblPwd= tk.Label(f2, text = "Contraseña:", font =("verdana", 12));
		lblPwd.place(x = 65, y = 65, anchor ="center");

		txtPwd = tk.Entry(f2);
		txtPwd.place(x = 120, y = 50, width=145);
		
		lblHide= tk.Label(f2, text = "Red Oculta: ", font =("verdana", 12));
		lblHide.place(x = 66, y = 90, anchor ="center");

		cbxShow = ttk.Combobox(f2,state="readonly",values=["No","Si"]);
		cbxShow.current(0)
		cbxShow.place(x = 120, y = 78);

		btnGenerar = tk.Button(f2, text ="Generar QR", command = lambda: self.genera_code(f, txtSSID.get(), cbxSeg.get(), txtPwd.get(), cbxShow.get()));

		btnGenerar.place(x = 75, y = 115);
		btnGenerar.config(width=20, height=1);

		ventana.mainloop();
		

if __name__ == '__main__':

	objView = view();
	objView.ViewGenerateQR();
