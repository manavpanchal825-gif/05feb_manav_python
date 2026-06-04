from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Preformatted
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors

# Create PDF
doc = SimpleDocTemplate("Exam_Answers.pdf", pagesize=A4)

styles = getSampleStyleSheet()

# Custom styles
title_style = ParagraphStyle('Title', parent=styles['Title'], textColor=colors.darkblue)
question_style = ParagraphStyle('Question', parent=styles['Heading2'], textColor=colors.red)
answer_style = ParagraphStyle('Answer', parent=styles['Normal'])

content = []

def add_title(text):
    content.append(Paragraph(text, title_style))
    content.append(Spacer(1, 10))

def add_q(text):
    content.append(Paragraph(text, question_style))
    content.append(Spacer(1, 6))

def add_a(text):
    content.append(Paragraph(text, answer_style))
    content.append(Spacer(1, 6))

def add_code(text):
    content.append(Preformatted(text, styles['Code']))
    content.append(Spacer(1, 8))

# Title
add_title("LINUX / OS EXAM ANSWERS")

# ---------------- Q3(A) ----------------
add_q("Q.3 (A) 1) What is Shell?")
add_a("""
A Shell is a command-line interpreter in Linux/Unix that allows users to interact with the OS.
It acts as a bridge between user and kernel.

Functions:
• Executes commands
• Runs programs
• Manages files
• Supports scripting

Example: bash
""")

add_q("2) Variables statement (True/False)")
add_a("""
This statement is FALSE.

Special variables:
$? → Exit status
$$ → Process ID
$# → Argument count
$0 → Script name
$1, $2 → Arguments
""")

add_q("3) Full form of GUI")
add_a("GUI = Graphical User Interface")

add_q("4) Full form of KDE")
add_a("KDE = K Desktop Environment")

# ---------------- Q3(B) ----------------
add_q("Q.3 (B) 1) echo command")
add_a("echo is used to display text or variables.")
add_code("echo Hello\necho $HOME")

add_q("2) passwd command")
add_a("Used to change password.")
add_code("passwd username")

# ---------------- Q3(C) ----------------
add_q("Q.3 (C) 1) break statement")
add_a("Break stops loop immediately.")
add_code("""
for i in 1 2 3 4 5
do
 if [ $i -eq 3 ]
 then
  break
 fi
 echo $i
done
""")

add_q("2) continue statement")
add_a("Continue skips current iteration.")
add_code("""
for i in 1 2 3 4 5
do
 if [ $i -eq 3 ]
 then
  continue
 fi
 echo $i
done
""")

# ---------------- Q3(D) ----------------
add_q("Q.3 (D) 1) Odd Even Script")
add_code("""
echo "Enter number:"
read num

if [ $((num % 2)) -eq 0 ]
then
 echo "Even"
else
 echo "Odd"
fi
""")

add_q("2) Case Statement")
add_code("""
echo "Enter number:"
read n

case $n in
1) echo "One" ;;
2) echo "Two" ;;
*) echo "Invalid" ;;
esac
""")

# ---------------- Q4(A) ----------------
add_q("Q.4 (A) 1) GNOME")
add_a("GNU Network Object Model Environment")

add_q("2) GNOME Login")
add_a("Username, Password, Session, Power options")

add_q("3) Create Folder in Ubuntu")
add_a("Use GUI or command:")
add_code("mkdir foldername")

add_q("4) Window Manager")
add_a("Controls windows: open, close, move, resize")

# ---------------- Q5(A) ----------------
add_q("Q.5 (A) Full Forms")
add_a("""
LDAP = Lightweight Directory Access Protocol
DNS = Domain Name System
FTP = File Transfer Protocol
SMB = Server Message Block
""")

# ---------------- Q5(B) ----------------
add_q("Q.5 (B) WINS")
add_a("Resolves NetBIOS name to IP")

add_q("Web Server")
add_a("Serves web pages (Apache, Nginx)")

# ---------------- Q5(C) ----------------
add_q("Q.5 (C) DNS")
add_a("Converts domain to IP (www.google.com → IP)")

add_q("Firewall")
add_a("Protects network from unauthorized access")

# ---------------- Q5(D) ----------------
add_q("Q.5 (D) Samba")
add_code("""
sudo apt install samba
sudo systemctl start smbd
""")

add_q("Active Directory")
add_a("""
Used for:
• User management
• Security
• Central control
""")

# Build PDF
doc.build(content)

print("PDF Created Successfully!")