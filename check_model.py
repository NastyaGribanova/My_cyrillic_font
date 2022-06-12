import torch
from torchvision import transforms
from text_on_image import recognize_text

PATH = "models/googlenet_model.pt"

EXAMPLE_DEFAULT_TEXT = 'Cъешь же ещё этих мягких французских булок да выпей чаю'

EXAMPLE_TEXT_MAX_SIZE = 64

FONT_NAMES = [
    'Inter',
    'Montserrat',
    'Nunito',
    'Open+Sans',
    'Oswald',
    'PT+Sans',
    'Raleway',
    'Roboto',
    'Source+Sans+Pro',
    'Ubuntu']


def model_predict(img_path):
    model_res = torch.load(PATH)
    model_res.eval()

    preprocess = transforms.Compose([
        transforms.Resize((224, 224)),
        transforms.ToTensor(),
        transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])
    ])

    from PIL import Image
    img_mont = Image.open(img_path).convert('RGB')

    img_mont_preprocessed = preprocess(img_mont)

    batch_img_mont_tensor = torch.unsqueeze(img_mont_preprocessed, 0)

    out = model_res(batch_img_mont_tensor)

    return out[0].detach()


def get_predict(img_path):
    my_preds = model_predict(img_path)
    example = ''

    try:
        text = recognize_text(img_path)
        for (_, t, _) in text:
            example = example + t + ' '
    except Exception:
        example = EXAMPLE_DEFAULT_TEXT

    result = list()
    for idx, pred in enumerate(my_preds):
        result.append({
            'name': FONT_NAMES[idx],
            'style': f'style=font-family:{FONT_NAMES[idx]}',
            'example': example[:EXAMPLE_TEXT_MAX_SIZE],
            'predict': str(pred)
        })

    result.sort(key=lambda x: x['predict'], reverse=True)
    return result
