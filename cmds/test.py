import discord as dc
from discord.ext import commands
from core import Cog_Extension

class test(Cog_Extension):
    
    @commands.command(aliases = ["t-1"])
    async def test_1(self, ctx):
        """
            測試運行
        """

        await ctx.send("Hello World!")    

    @commands.command(aliases = ["t-2"])
    async def test_2(self, ctx):
        """
            讓我們看看 ctx 這個參數裡面有甚麼 ?
        """

        # await ctx.send(f"the variable (ctx) includes the following : \n{ctx}\n")

        # ctx.message 擷取出來的是 ... ?
        await ctx.send(f"the variable (ctx.message) includes the following : \n{ctx.message}\n")
        # # ctx.message.content 擷取出來的是 ... ?
        # await ctx.send(f"the variable (ctx.message.content) includes the following : \n{ctx.message.content}\n")
        # # 型態是 ?
        # await ctx.send(f"type is : \n{type(ctx.message.content)}\n")

    @commands.command(aliases = ["t-3"])
    async def test_3(self, ctx):
        """
            讓我們在 bot 上做一個 "輸出使用者輸入" 的程式
        """

        # 利用這個 ctx 是不是可以完成輸入輸出，而不需要依賴 on_message() ?

        """
            e.g. in Python 模擬

            user_input = input()
            print(user_input)

            (
                小撇步：關於自定義函數到 bot 上
                
                可以先在本地先單純用 python 做好，編譯執行。
                之後再放到 bot 裡，只需要改輸入、輸出的部分。
                (記得注意變數的型態變化)
            )
        """

        # write in discord bot...

        # 函式：獲取使用者輸入
        def user_input() -> str:

            message = ctx.message.content

            # 取出完整的 input 內容，(去除指令名稱 <test_input> + 一個空格即可)
            user_message = "" + message[9 : len(message)]

            return user_message


        await ctx.send(f"output : \n{user_input()}")  
    

def setup(bot):
    bot.add_cog(test(bot))