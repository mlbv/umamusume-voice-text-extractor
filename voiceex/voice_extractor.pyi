from typing import List

class UmaVoiceEx:
    def __init__(self, acbPath: str, awbPath: str):
        """
        From voice_ex.cs
        :param acbPath: acb file path
        :param awbPath: awb file path
        """
        ...
    @staticmethod
    def GetSaveName(savePath: str, saveFileprefix: str, waveId: int) -> str: ...
    def ExtractAudioFromWaveId(self, savePath: str, saveFileprefix: str, waveId: int) -> str: ...
    def ExtractAudioFromCueId(self, savePath: str, saveFileprefix: str, cueId: int, gender : int = 0) -> str: ...
    def SetWaveFormat(self, rate: int, bits: int, channels: int): ...
    def GetWaveIds(self) -> List[int]: ...
    def GetAudioCount(self) -> int: ...
    def SetVolume(self, value: float): ...
    @staticmethod
    def GetStreamCriAuthKey(umaInstallPath: str) -> int: ...
    @staticmethod
    def CutWavFile(fileName: str, saveName: str, startMs: int, endMs: int) -> None: ...
    @staticmethod
    def CutWavFileBatch(fileName: str, saveNamePrefix: str, timeMsList): ...
    @staticmethod
    def ResampleWav(fileName: str, saveName: str, rate: int, bits: int, channels: int) -> None: ...
    @staticmethod
    def MixWav(files, saveName: str, volume: float): ...
    @staticmethod
    def RemoveAudioSilence(fileName: str): ...
    @staticmethod
    def ConcatenateWavFiles(outputFile: str, sourceFiles): ...
    @staticmethod
    def SilenceWavPartsByActivePos(fileName: str, saveName: str, activeMs): ...
    def Close(self): ...
