import json

class PrettyDatePrint:
    def __init__(self, fontFilePath) -> None:
        self.fontFilePath = fontFilePath
        with open(fontFilePath, "r", encoding="utf-8") as f:
            self.fontFile = json.load(f)
        
        self.fontHeight = self.fontFile["metadata"]["height"]
        self.fontSpaceWidth = self.fontFile["metadata"]["SpaceWidth"]
        self.font = self.fontFile["font"]

    def applyFont(self, string):
        outLines = [""] * self.fontHeight

        for i in range(len(string)):
            char = string[i]
            #print(f'char: {char}, index: {i}')
            if char in self.font:
                charFont = self.font[char]
            else:
                charFont = self.font["unknown"]

            for j in range(self.fontHeight):
                outLines[j] += charFont[j] + (" " * self.fontSpaceWidth if i != len(string) - 1 else "")
            
        return outLines
        
    def boxBuilder(self,lines, hSpacing=1, vSpacing=1):
        maxLineLength = max(len(line) for line in lines)
        lineWidth = maxLineLength + 2 * hSpacing

        topBorder = "+" + "-" * lineWidth + "+"
        bottomBorder = topBorder

        middlePart = []
        middlePart += ["|" + " " * lineWidth + "|"] * vSpacing
        for line in lines:
            paddedLine = "|" + " " * hSpacing + line + " " * hSpacing + "|"
            middlePart.append(paddedLine)
        middlePart += ["|" + " " * lineWidth + "|"] * vSpacing

        box = [topBorder] + middlePart + [bottomBorder]
        return "\n".join(box)

    def prettyDatePrint(self, day, month, year, sep="."):
        dateString = sep.join([f'{day:02d}', f'{month:02d}', f'{year:04d}'])
        #print(dateString)
        outLines = self.applyFont(dateString)
        outString = self.boxBuilder(outLines, hSpacing=2, vSpacing=0)
        return outString 