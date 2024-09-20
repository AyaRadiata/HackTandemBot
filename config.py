
TOKEN = "7052272805:AAHI5uowpda4HL-HqR_vkTSXxUS-7gDMwog"

OPENAI_SK = "sk-a3LJ6z-ntaYMW9Fqb3SQoQwMa2gdDEj3aRWdGp1DVrT3BlbkFJTIS2H-DzOq3--VPGCmlC__Y-N0hjVTlsUzcIQOCPoA"

COUNSELOR_TG_ID = '1391115076'

maxAITrials = 2

files = [
    {
        "fileName": "Student Brag Sheet  📑",
        "filePath": "files/BragSheet.docx",
        "fileBtnCallback": "f_bragSheet"
    },
    {
        "fileName": "Common App Guide  📲",
        "filePath": "files/CommonAppGuide.pdf",
        "fileBtnCallback": "f_commonAppGuide"
    }
]

first_menu = [
    {
        "option": "Let's Start 🏃‍➡️",
        "callback": "fm_start"
    },
    {
        "option": "What Can You Do? 📌",
        "callback": "fm_wcyd"
    },
    {
        "option": "Councilor Contacts ☎️",
        "callback": "fm_contacts"
    }
]

menuText = "📌📌📌📌 MENU 📌📌📌📌 \n\n\n\n\n Choose an option below:"

menu = [
    {
        "option": "files 📑",
        "callback": "menuBtnFiles"
    },
    {
        "option": "Q&A ❓",
        "callback": "menuBtnQA"
    },
    {
        "option": "Ask our AI 👀",
        "callback": "menuAI"
    },
    {
        "option": "Determine your career 💼",
        "callback": "menuCareer"
    },
    {
        "option": "Reg in 📲",
        "callback": "reg_in"
    },
    {
        "option": "Book an appointment 📨",
        "callback": "appBook"
    }
]

allQA = [
    {
        "Q": "What does the school councselor do?",
        "A": "School councilor provides you with the main information that is needed for you to apply to universities."
    },
    {
        "Q": "What is Scholarship?",
        "A": "Scholarship is a financial help for students that want to apply to colleges."
    }
]

contacts = [
    {
        "contact": "Telegram 📨",
        "url": "https://web.telegram.org/a/#93372553"
    },
    {
        "contact": "Whatsapp 📞",
        "url": "https://wa.me/77072517728"
    }
]

careerDeterminationLinks = [
    {
        "careerTestName": "Профессиональные типы Холланда",
        "careerTestLink": "https://psytests.org/profession/hollandA-run.html"
    },
    {
        "careerTestName": "Профессиональные склонности (Йоваши-Резапкина)",
        "careerTestLink": "https://psytests.org/profession/yovrez-run.html"
    }
]
