import pip
import asyncio
import os


def checkModule():
    try:
        from waifuim import WaifuAioClient
        import requests
        import PIL
        return
    except:
        pip.main(['install', 'waifuim.py'])
        pip.main(['install', 'requests'])
        pip.main(['install', 'pillow'])
        return


async def main():
    from waifuim import WaifuAioClient
    import requests
    from PIL import Image

    wf = WaifuAioClient()
    
    # Get a completely random image
    boobPics = await wf.random(orientation=['LANDSCAPE'], many=True)
    
 
    await wf.close()
    
    # You can also use a context manager but for multiple request it is not recommended
    
    async with WaifuAioClient() as wf:
        if not os.path.exists('theVault'):
            os.makedirs('theVault/raw')
            os.makedirs('theVault/refined')

        print("Downloading waifus!\n")

        for boobs in boobPics:
            rawBoob = requests.get(boobs)
            filename = str(boobs).split("/").pop()
            open('theVault/raw/' + filename, "wb").write(rawBoob.content)
            
            treatBoob = Image.open('theVault/raw/' + filename)
            size = (1280, 768)
            refinedBoob = treatBoob.resize(size)
            refinedBoob.save("theVault/refined/" + str(size) + " " + filename)
            print("Waifu", filename, "acquired")



if __name__ == "__main__":
    checkModule()
    asyncio.run(main())
