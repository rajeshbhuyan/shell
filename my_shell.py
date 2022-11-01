import cmd
import os
class my_shell(cmd.Cmd):
    prompt = 'rajesh> '
    intro = "Welcome to my new shell"
    # print ("Hello Friends!! two commands are added")
    def do_exit(self, inp_string):
       print("Bye")
       return True
    def do_echo(self,inp_string):
       print(inp_string)
    def do_ls(self,inp_string):
       os.system("/usr/bin/ls")
    def do_prompt(self,inp_string):
       PS1=inp_string+"$ "
       self.prompt = PS1 #inp_string
    do_EOF = do_exit

shell = my_shell()
shell.cmdloop()
