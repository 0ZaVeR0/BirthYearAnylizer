import json

class PrettyDatePrint:
    def __init__(self, fontFilePath) -> None:
        self.fontFilePath = fontFilePath
        with open(fontFilePath, "r", encoding="utf-8") as f:
            self.fontFile = json.load(f)
        
        self.fontHeight = self.fontFile["metadata"]["height"]
        self.fontSpaceWidth = self.fontFile["metadata"]["SpaceWidth"]
        self.font = self.fontFile["font"]

    def __applyFont(self, string: str) -> list[str]:
        """Applies font to input string and returns array of lines"""
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
        
    def __boxBuilder(self, lines: list[str], hSpacing=1, vSpacing=1) -> str:
        """Builds box around lines with specified spacings. Returns joined string"""
        maxLineLength = max(len(line) for line in lines)
        lineWidth = maxLineLength + 2 * hSpacing

        hBorder = "+" + "-" * lineWidth + "+"

        middlePart = []
        middlePart += ["|" + " " * lineWidth + "|"] * vSpacing
        for line in lines:
            paddedLine = "|" + " " * hSpacing + line + " " * hSpacing + "|"
            middlePart.append(paddedLine)
        middlePart += ["|" + " " * lineWidth + "|"] * vSpacing

        box = [hBorder] + middlePart + [hBorder]
        return "\n".join(box)

    def prettyDatePrint(self, day: int, month: int, year: int, sep=".", boxHSpacing=2, boxVSpacing=0) -> str:
        """Returns date with font applied and box around it"""
        dateString = sep.join([f'{day:02d}', f'{month:02d}', f'{year:04d}'])
        #print(dateString)
        outLines = self.__applyFont(dateString)
        outString = self.__boxBuilder(outLines, boxHSpacing, boxVSpacing)
        return outString 