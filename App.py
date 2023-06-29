from Interface import Interface

class App:
    def __init__(self):
        self.interface = Interface()
        self.interface.window.mainloop()

if __name__ == "__main__":
    app = App()
