@bot.command()
async def report(ctx, member: discord.member, arg: str):
    em = discord.Embed(title="Report",description="Ein Neuer Report!",colour=0)
    em.add_field(name="Report Ersteller:",value=f"{ctx.author.mention}")
    em.add_field(name="Reporteter User:",value=f"{member.mention}")
    em.add_field(name="Grund",value=f"{arg}")
    em.add_field(name="Erstellt in:",value=f"{ctx.channel.mention}")
    em.timestamp = datetime.datetime.utcnow()
    rchannel = bot.get_channel(id=925887479523971113)
    em = rchannel.send(embed=em)
    ##############################################
    bm = discord.Embed(title="Danke für deine Report!",description=f"Du hast {member.mention} wegen {arg} gemeldet!",color=0)
    bm.set_footer(text="Der Support wird sich in Kürze um dein Report Kümmern!")
    await ctx.author.send(embed=em)
    await ctx.message.delete()
