import os
import cv2

_save_files = True


def set_save_files(flag: bool):
    global _save_files
    _save_files = flag


def get_save_files():
    return _save_files


def ensure_dir(filename):
    """
    根据图片名创建保存中间结果的文件夹。
    例如 filename = frame_0.jpg
    会创建 outputs/frame_0/
    """
    base_name = os.path.splitext(os.path.basename(filename))[0]
    save_path = os.path.join("outputs", base_name)

    if not os.path.exists(save_path):
        os.makedirs(save_path)

    return save_path


def save_dir(img, prefix, filename):
    """
    保存图像到 outputs/文件名/ 文件夹下。
    如果 set_save_files(False)，则不保存，只返回原图。
    """
    if _save_files and filename:
        save_path = ensure_dir(filename)
        out_name = prefix + os.path.basename(filename)
        out_path = os.path.join(save_path, out_name)
        cv2.imwrite(out_path, img)

    return img