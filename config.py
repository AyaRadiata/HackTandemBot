# TOKEN = "7217611606:AAEhTEpiylRRcsJcsTHq13wWye7H0vosXI8"
TOKEN = "7052272805:AAHI5uowpda4HL-HqR_vkTSXxUS-7gDMwog"

OPENAI_SK = "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"

COUNSELOR_TG_ID = '1391115076'

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
        "option": "Ask our AI 📲",
        "callback": "menuAI"
    },
    {
        "option": "Determine your career 💼",
        "callback": "menuCareer"
    },
    {
        "option": "Reg in",
        "callback": "reg_in"
    },
    {
        "option": "Book an appointment",
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