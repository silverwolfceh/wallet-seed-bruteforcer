import tkinter as tk
import json
import tkinter.font as tkFont
from enum import Enum
from app import start_app, stop_app

class APPSTATE(Enum):
	STOP  =  0
	START = 1


class App:
	def __init__(self, root, version, preconfig):
		#setting title
		root.title(f"Wallet Scanner V{version}")
		root.iconbitmap("icon.ico")
		#setting window size
		width=400
		height=600
		screenwidth = root.winfo_screenwidth()
		screenheight = root.winfo_screenheight()
		alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
		root.geometry(alignstr)
		root.resizable(width=False, height=False)

		self.eth_var = tk.BooleanVar()
		self.btc_var = tk.BooleanVar()
		self.bnb_var = tk.BooleanVar()
		self.sol_var = tk.BooleanVar()
		self.max_thread = 0
		self.telechat_var = tk.StringVar()
		self.state = APPSTATE.STOP

		self.txt_log= tk.Text(root, wrap="word")
		self.txt_log["borderwidth"] = "1px"
		ft = tkFont.Font(family='Times',size=10)
		self.txt_log["font"] = ft
		self.txt_log["fg"] = "#333333"
		self.txt_log.insert("1.0", "Running log") 
		self.txt_log.place(x=0,y=60,width=394,height=183)

		lbl_banner=tk.Label(root)
		lbl_banner["bg"] = "#90f090"
		ft = tkFont.Font(family='Times',size=13)
		lbl_banner["font"] = ft
		lbl_banner["fg"] = "#c71585"
		lbl_banner["justify"] = "center"
		lbl_banner["text"] = f"Wallet Scanner V{version}"
		lbl_banner["relief"] = "flat"
		lbl_banner.place(x=0,y=0,width=399,height=30)

		GLabel_107=tk.Label(root)
		ft = tkFont.Font(family='Times',size=12)
		GLabel_107["font"] = ft
		GLabel_107["fg"] = "#333333"
		GLabel_107["justify"] = "center"
		GLabel_107["text"] = "Scanning"
		GLabel_107.place(x=0,y=30,width=70,height=25)

		GLabel_622=tk.Label(root)
		ft = tkFont.Font(family='Times',size=12)
		GLabel_622["font"] = ft
		GLabel_622["fg"] = "#333333"
		GLabel_622["justify"] = "center"
		GLabel_622["text"] = "Settings"
		GLabel_622.place(x=0,y=250,width=70,height=25)

		ckb_eth=tk.Checkbutton(root)
		ft = tkFont.Font(family='Times',size=10)
		ckb_eth["font"] = ft
		ckb_eth["fg"] = "#333333"
		ckb_eth["justify"] = "center"
		ckb_eth["text"] = "ETH"
		ckb_eth.place(x=0,y=280,width=70,height=25)
		ckb_eth["offvalue"] = "0"
		ckb_eth["onvalue"] = "1"
		ckb_eth["variable"] = self.eth_var
		ckb_eth["command"] = self.coin_selection_update

		ckb_btc=tk.Checkbutton(root)
		ft = tkFont.Font(family='Times',size=10)
		ckb_btc["font"] = ft
		ckb_btc["fg"] = "#333333"
		ckb_btc["justify"] = "center"
		ckb_btc["text"] = "BTC"
		ckb_btc.place(x=90,y=280,width=70,height=25)
		ckb_btc["offvalue"] = "0"
		ckb_btc["onvalue"] = "1"
		ckb_btc["variable"] = self.btc_var
		ckb_btc["command"] = self.coin_selection_update

		ckb_bnb=tk.Checkbutton(root)
		ft = tkFont.Font(family='Times',size=10)
		ckb_bnb["font"] = ft
		ckb_bnb["fg"] = "#333333"
		ckb_bnb["justify"] = "center"
		ckb_bnb["text"] = "BNB"
		ckb_bnb.place(x=180,y=280,width=70,height=25)
		ckb_bnb["offvalue"] = "0"
		ckb_bnb["onvalue"] = "1"
		ckb_bnb["variable"] = self.bnb_var
		ckb_bnb["command"] = self.coin_selection_update

		ckb_sol=tk.Checkbutton(root)
		ft = tkFont.Font(family='Times',size=10)
		ckb_sol["font"] = ft
		ckb_sol["fg"] = "#333333"
		ckb_sol["justify"] = "center"
		ckb_sol["text"] = "SOL"
		ckb_sol.place(x=270,y=280,width=70,height=25)
		ckb_sol["offvalue"] = "0"
		ckb_sol["onvalue"] = "1"
		ckb_sol["variable"] = self.sol_var
		ckb_sol["command"] = self.coin_selection_update

		self.txt_teletoken=tk.Entry(root)
		self.txt_teletoken["borderwidth"] = "1px"
		ft = tkFont.Font(family='Times',size=10)
		self.txt_teletoken["font"] = ft
		self.txt_teletoken["fg"] = "#333333"
		self.txt_teletoken["justify"] = "center"
		self.txt_teletoken["text"] = "Telegram Token"
		# txt_teletoken["variable"] = self.teletoken_var
		self.txt_teletoken.place(x=10,y=310,width=171,height=30)

		self.txt_telechatid=tk.Entry(root)
		self.txt_telechatid["borderwidth"] = "1px"
		ft = tkFont.Font(family='Times',size=10)
		self.txt_telechatid["font"] = ft
		self.txt_telechatid["fg"] = "#333333"
		self.txt_telechatid["justify"] = "center"
		self.txt_telechatid["text"] = "Telegram Chat ID"
		self.txt_telechatid.place(x=190,y=310,width=203,height=30)

		btn_start=tk.Button(root)
		btn_start["bg"] = "#f0f0f0"
		ft = tkFont.Font(family='Times',size=10)
		btn_start["font"] = ft
		btn_start["fg"] = "#000000"
		btn_start["justify"] = "center"
		btn_start["text"] = "Start"
		btn_start.place(x=10,y=350,width=109,height=30)
		btn_start["command"] = self.btn_start_command

		btn_config=tk.Button(root)
		btn_config["bg"] = "#f0f0f0"
		btn_config["font"] = ft
		btn_config["fg"] = "#000000"
		btn_config["justify"] = "center"
		btn_config["text"] = "LoadConfig"
		btn_config.place(x=125,y=350,width=100,height=30)
		btn_config["command"] = self.btn_load_config

		btn_export=tk.Button(root)
		btn_export["bg"] = "#f0f0f0"
		ft = tkFont.Font(family='Times',size=10)
		btn_export["font"] = ft
		btn_export["fg"] = "#000000"
		btn_export["justify"] = "center"
		btn_export["text"] = "Export Result"
		btn_export.place(x=230,y=350,width=203,height=30)
		btn_export["command"] = self.btn_export_command

		self.txt_found=tk.Text(root, wrap="word")
		self.txt_found["borderwidth"] = "1px"
		ft = tkFont.Font(family='Times',size=10)
		self.txt_found["font"] = ft
		self.txt_found["fg"] = "#333333"
		self.txt_found.insert("1.0", "Found log")
		self.txt_found.place(x=0,y=410,width=396,height=120)

		btn_zalo=tk.Button(root)
		btn_zalo["bg"] = "#f0f0f0"
		ft = tkFont.Font(family='Times',size=10)
		btn_zalo["font"] = ft
		btn_zalo["fg"] = "#000000"
		btn_zalo["justify"] = "center"
		btn_zalo["text"] = "Zalo"
		btn_zalo.place(x=40,y=550,width=70,height=25)
		btn_zalo["command"] = self.btn_zalo_command

		GLabel_105=tk.Label(root)
		ft = tkFont.Font(family='Times',size=12)
		GLabel_105["font"] = ft
		GLabel_105["fg"] = "#333333"
		GLabel_105["justify"] = "center"
		GLabel_105["text"] = "Found"
		GLabel_105.place(x=0,y=380,width=61,height=30)

		btn_discord=tk.Button(root)
		btn_discord["bg"] = "#f0f0f0"
		ft = tkFont.Font(family='Times',size=10)
		btn_discord["font"] = ft
		btn_discord["fg"] = "#000000"
		btn_discord["justify"] = "center"
		btn_discord["text"] = "Discord"
		btn_discord.place(x=150,y=550,width=70,height=25)
		btn_discord["command"] = self.btn_discord_command

		btn_email=tk.Button(root)
		btn_email["bg"] = "#f0f0f0"
		ft = tkFont.Font(family='Times',size=10)
		btn_email["font"] = ft
		btn_email["fg"] = "#000000"
		btn_email["justify"] = "center"
		btn_email["text"] = "Email"
		btn_email.place(x=270,y=550,width=70,height=25)
		btn_email["command"] = self.btn_email_command

	
	def coin_selection_update(self):
		eth_enable = self.eth_var.get()
		btc_enable = self.btc_var.get()
		bnb_enable = self.bnb_var.get()
		sol_enable = self.sol_var.get()
		print(f"ETH: {eth_enable} | BTC: {btc_enable} | BNB: {bnb_enable} | SOL: {sol_enable}")


	def btn_start_command(self):
		if self.state == APPSTATE.STOP:
			start_app(self.running_log, self.found_log)
			self.state = APPSTATE.START
		else:
			stop_app()
			self.state = APPSTATE.STOP


	def btn_export_command(self):
		print("command")


	def btn_zalo_command(self):
		print("command")


	def btn_discord_command(self):
		print("Discord")


	def btn_email_command(self):
		print("command")

	def append_text(self, widget, msg):
		widget.insert(tk.END, msg)
		widget.see(tk.END)  

	def running_log(self, msg):
		self.txt_log.after(0, self.append_text, self.txt_log, msg)

	def found_log(self, msg):
		self.txt_found.after(0, self.append_text, self.txt_found, msg)

	def btn_load_config(self):
		with open("config.json") as f:
			data = json.loads(f.read())
			for k, v in data["SUPPORT_COIN"].items():
				c = k.lower()
				var = getattr(self, f"{c}_var")
				var.set(True)
			self.txt_teletoken.delete(0, tk.END)  
			self.txt_teletoken.insert(0, data["TELE_TOKEN"])
			self.txt_telechatid.delete(0, tk.END)
			self.txt_telechatid.insert(0, data["TELE_CHAN_ID"])

				
		print("Load config")

if __name__ == "__main__":
	ver = "3"
	config = []
	root = tk.Tk()
	app = App(root, ver, config)
	root.mainloop()
