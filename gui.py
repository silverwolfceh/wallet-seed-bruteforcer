import tkinter as tk
import queue
import tkinter.font as tkFont
from enum import Enum
import webbrowser
from app import start_app, stop_app
from config import configcls, COINSTR, coin_to_path, CONFIGSTR
from util import init_telegram, send_found
from fileio import safefilewriter

class APPSTATE(Enum):
	STOP  =  0
	START = 1


class App:
	def __init__(self, root, version):
		self.var_init()
		#setting title
		root.title(f"ETH Wallet Scanner V{version}")
		root.iconbitmap("icon.ico")
		#setting window size
		width=400
		height=600
		screenwidth = root.winfo_screenwidth()
		screenheight = root.winfo_screenheight()
		alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
		root.geometry(alignstr)
		root.resizable(width=False, height=False)

		self.txt_log= tk.Text(root, wrap="word")
		self.txt_log["borderwidth"] = "1px"
		ft = tkFont.Font(family='Times',size=10)
		self.txt_log["font"] = ft
		self.txt_log["fg"] = "#333333"
		# self.txt_log.insert("1.0", "Running log") 
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

		self.btn_start=tk.Button(root)
		self.btn_start["bg"] = "#f0f0f0"
		ft = tkFont.Font(family='Times',size=10)
		self.btn_start["font"] = ft
		self.btn_start["fg"] = "#000000"
		self.btn_start["justify"] = "center"
		self.btn_start["text"] = "Start"
		self.btn_start.place(x=10,y=350,width=109,height=30)
		self.btn_start["command"] = self.btn_start_command

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

	def var_init(self):
		self.eth_var = tk.BooleanVar()
		self.btc_var = tk.BooleanVar()
		self.bnb_var = tk.BooleanVar()
		self.sol_var = tk.BooleanVar()
		self.telechat_var = tk.StringVar()
		self.state = APPSTATE.STOP
		self.config = configcls()
		self.max_thread = self.config.get("MAX_THREAD", 20)
		self.wthread = {}
		self.support_list = ["btc", "eth", "sol", "bnb"]
		self.wq = queue.Queue()
		self.fthread = safefilewriter(self.wq)
		self.fthread.start()
	
	def coin_selection_update(self):
		scoins = {}
		for c in self.support_list:
			is_enable = getattr(self, f"{c}_var").get()
			if is_enable:
				scoins[c] = coin_to_path(c)
		self.config.set(CONFIGSTR.SUPPORT_COIN.value, scoins)


	def stop_app_done(self):
		self.btn_start.configure(state=tk.NORMAL)
		self.btn_start["text"] = "Start"

	def btn_start_command(self):
		if self.state == APPSTATE.STOP:
			self.running_log("Starting the app.... \n")
			self.wthread = start_app(self.running_log, self.found_log)
			self.state = APPSTATE.START
			self.btn_start["text"] = "Stop"
		else:
			self.running_log("Stopping the app.... \n")
			stop_app(self.wthread, self.stop_app_done)
			self.state = APPSTATE.STOP
			self.btn_start["text"] = "Stopping..."
			self.btn_start.configure(state=tk.DISABLED)



	def btn_export_command(self):
		print("command")


	def btn_zalo_command(self):
		url = "https://zalo.me/g/wwtwfk998"
		webbrowser.open_new_tab(url)


	def btn_discord_command(self):
		url = "https://discordapp.com/users/753230071195631707"
		webbrowser.open_new_tab(url)


	def btn_email_command(self):
		url = "mailo:evisrss1@gmail.com?subject=Wallet+Scanner+V3"
		webbrowser.open_new_tab(url)

	def append_text(self, widget, msg):
		widget.insert(tk.END, msg)
		widget.see(tk.END)  

	def running_log(self, msg):
		self.txt_log.after(0, self.append_text, self.txt_log, msg)

	def found_log(self, w, coin, bl):
		send_found(self.wq, self.txt_teletoken.get(), self.txt_telechatid.get(), w, coin, bl)
		msg = f"[{coin}] Balance: {bl} - {w} \n"
		self.txt_found.after(0, self.append_text, self.txt_found, msg)

	def btn_load_config(self):
		support_coins = self.config.get("SUPPORT_COIN", {})
		for k, v in support_coins.items():
			# Check and uncheck for coins
			c = k.lower()
			var = getattr(self, f"{c}_var")
			var.set(True)
		
		self.txt_teletoken.delete(0, tk.END)  
		self.txt_teletoken.insert(0, self.config.get("TELE_TOKEN", "7160327586:AAFFuwwZ4IW3WV0GalBzSqOOrDUk2vXULX0"))
		self.txt_telechatid.delete(0, tk.END)
		self.txt_telechatid.insert(0, self.config.get("TELE_CHAN_ID", "5624258194"))
		init_telegram(self.txt_teletoken.get(), self.txt_telechatid.get())
		self.running_log("Configuration was loaded \n")

if __name__ == "__main__":
	ver = "3"
	config = []
	root = tk.Tk()
	app = App(root, ver)
	root.mainloop()
