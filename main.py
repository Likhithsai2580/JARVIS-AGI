# ██████╗   ███████╗ ██╗    ██╗ ███████╗            ██████╗    ██████╗             ██████╗   ██████╗    ██████╗   ███████╗
# ██╔══██╗ ██╔════╝ ██║    ██║ ██╔════╝            ██╔══██╗ ██╔═══██╗          ██╔════╝ ██╔═══██╗ ██╔══██╗ ██╔════╝
# ██║    ██║ █████╗     ██║    ██║ ███████╗            ██║    ██║ ██║      ██║         ██║          ██║      ██║ ██║    ██║ █████╗  
# ██║    ██║ ██╔══╝    ╚██╗  ██╔╝ ╚════██║           ██║    ██║ ██║      ██║         ██║          ██║      ██║ ██║    ██║ ██╔══╝  
# ██████╔╝ ███████╗  ╚████╔╝  ███████║            ██████╔╝╚██████╔╝          ╚██████╗ ╚██████╔╝  ██████╔╝ ███████╗
# ╚═════╝  ╚══════╝    ╚═══╝     ╚══════╝            ╚═════╝    ╚═════╝             ╚═════╝   ╚═════╝    ╚═════╝   ╚══════╝

#  Made With 💓 By - Sree ( Devs Do Code )
#  YouTube Channel: https://www.youtube.com/@devsdocode

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

      - Support: https://buymeacoffee.com/devsdocode
      - Patreon: https://patreon.com/DevsDoCode

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

#  For any questions or concerns, reach out to us via our social media handles.
#  Our top choice for contact is Telegram: https://t.me/devsdocode
#  You can also find us on other platforms listed above. We're here to help!

#  - YouTube Channel: https://www.youtube.com/@DevsDoCode
#  - Telegram Group: https://t.me/devsdocode
#  - Discord Server: https://discord.gg/ehwfVtsAts
#  - Instagram:
#    - Personal: https://www.instagram.com/sree.shades_/
#    - Channel: https://www.instagram.com/devsdocode_/

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

    - Support: https://buymeacoffee.com/devsdocode
    - Patreon: https://patreon.com/DevsDoCode

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
#  ------------------------------------------------------------------------------
#  Dive into the world of coding with Devs Do Code - where passion meets programming!
#  Make sure to hit that Subscribe button to stay tuned for exciting content!

#  Pro Tip: For optimal performance and a seamless experience, we recommend using
#  the default library versions demonstrated in this demo. Your coding journey just
#  got even better! Happy coding!
#  ----------------------------------------------------------------------------

"""-------------------------------------------------------------------------------------------------IMPORTS-------------------------------------------------------------------------------------------------"""
import concurrent.futures
import os

# from ENGINE.STT.vosk_recog import speech_to_text
from ENGINE.STT.NetHyTech import SpeechToTextListener; listener = SpeechToTextListener()

# from ENGINE.TTS.edge_tts import speak
# from ENGINE.TTS.deepAI import speak
# from ENGINE.TTS.ai_voice import speak, initiate_proxies
from ENGINE.TTS.stream_elements_api import speak

from BRAIN.AI.TEXT.API import deepInfra_TEXT
from BRAIN.AI.TEXT.API import openrouter
# from BRAIN.AI.TEXT.API import liaobots
# from BRAIN.AI.TEXT.API import hugging_chat; hf_api = hugging_chat.HuggingChat_RE(model="microsoft/Phi-3-mini-4k-instruct")
# from BRAIN.AI.TEXT.API import Blackbox_ai
# from BRAIN.AI.TEXT.API import Phind

from BRAIN.AI.VISION import deepInfra_VISION

# from BRAIN.TOOLS import groq_web_access

# from BRAIN.AI.IMAGE import deepInfra_IMG

# from PLAYGROUND.ADB_CALL import make_call, android_device_connection_setup; android_device_connection_setup.initialise()
from PLAYGROUND.WEBSITE_ASSISTANT import jenna_reader, chrome_latest_url
from PLAYGROUND.CAMERA import camera_vision

from PROMPTS import INSTRUCTIONS, BISECTORS

"""-------------------------------------------------------------------------------------------------MAIN-----------------------------------------------------------------------------------------------------"""

# for speech in speech_to_text():
while True:
    speech = listener.listen()   
    print("Human >>", speech)

    response_img_or_text = concurrent.futures.ThreadPoolExecutor().submit(deepInfra_TEXT.generate, speech, system_prompt=BISECTORS.image_requests_v2)
    response_classifier = concurrent.futures.ThreadPoolExecutor().submit(deepInfra_TEXT.generate, speech, system_prompt=BISECTORS.complex_task_classifier_v5, stream=False)
    default_response = concurrent.futures.ThreadPoolExecutor().submit(deepInfra_TEXT.generate, speech, system_prompt=INSTRUCTIONS.human_response_v3_AVA, stream=False)
    
    concurrent.futures.wait([response_img_or_text, response_classifier, default_response])
    print("Classifier >> ", "\033[91m" + response_classifier.result() + "\033[0m")

    if "vision" in response_classifier.result().lower():
        concurrent.futures.ThreadPoolExecutor().submit(speak("Analysing, Please Wait"))
        image_path = camera_vision.realtime_vision()
        response_vison = deepInfra_VISION.generate(speech, system_prompt=INSTRUCTIONS.vison_realtime_v1, image_path=image_path)
        print("AI>>", response_vison)
        os.remove(image_path)
        speak(response_vison)

    elif "call" in response_classifier.result().lower():
        speak("Sure Sir. Calling")
        # make_call.call()

    elif "website" in response_classifier.result().lower():
        site_markdown = jenna_reader.fetch_website_content(chrome_latest_url.get_latest_chrome_url())
        response = openrouter.generate(f"METEDATA: {site_markdown}\n\nQUERY: {speech}", system_prompt="Keep you responses very short and concise")
        speak(response, voice="Salli")

    else: 
        print("AI>>", default_response.result())
        speak(default_response.result())















    # ai_response = Phind.generate(speech, stream=False)
    # ai_response = openrouter.generate(speech, stream=False)
    # ai_response = hf_api.generate(speech, stream=False)
    # ai_response = liaobots.generate(speech)
    # ai_response = groq_web_access.generate(speech)
    # ai_response = openrouter.generate(speech)
    # ai_response = deepInfra_TEXT.generate(speech)
    # sources, ai_response = Blackbox_ai.generate(speech, system_prompt="Keep your Responses very short and concise", web_access=True, stream=False)
        
    # print("AI >>", ai_response.replace("@web_search", ""))
    # speak(ai_response)

    # if 'call' in speech:
    #     speak("Sure Sir. Calling")
    #     make_call.call()

    # speak("Sure sir, generating images for you")
    # images_link = deepInfra_IMG.generate(speech)
    # print(images_link)

