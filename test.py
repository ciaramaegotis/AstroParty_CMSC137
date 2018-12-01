sample = "aksjdhiahshdjiahsdahsdaspkdjewouifhewuifhiuwefihqewnfdouqeuyfgq"
toPrint = []
for i in range(0, len(sample), 22):
    toPrint.append(sample[i:i+22])

for i in toPrint:
    print(i)

            for trans in chat_transcript:
            for i in range(0, len(trans), 22):
                toPrint.append(trans[i:i+22])
            for i in toPrint:
                label = myfont.render(i, 1, (255,255,255))
                screen.blit(label, (30, start_y))
                start_y += 20