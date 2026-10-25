import lab2
from unittest.mock import patch


def test_loadFromCSV(tmp_path):
    fileName = tmp_path / "students.csv"
    fileName.write_text(
        "name,phone,email,group\n"
        "Bob,0631234567,bob@gmail.com,KB-251\n",
        encoding="utf-8"
    )

    lab2.list.clear()
    lab2.loadFromCSV(fileName)

    assert len(lab2.list) == 1
    assert lab2.list[0]["name"] == "Bob"
    assert lab2.list[0]["group"] == "KB-251"


def test_saveToCSV(tmp_path):
    lab2.list.clear()
    lab2.list.append({
        "name": "Dima",
        "phone": "0631234567",
        "email": "dima@gmail.com",
        "group": "KB-261"
    })

    fileName = tmp_path / "students.csv"
    lab2.saveToCSV(fileName)

    content = fileName.read_text(encoding="utf-8")
    assert "Dima" in content
    assert "KB-261" in content


def test_addNewElement():
    lab2.list.clear()

    with patch("builtins.input", side_effect=[
        "Dima", "0631234567", "dima@gmail.com", "KB-261"
    ]):
        lab2.addNewElement()

    assert len(lab2.list) == 1
    assert lab2.list[0]["name"] == "Dima"


def test_deleteElement():
    lab2.list.clear()
    lab2.list.append({
        "name": "Dima",
        "phone": "0631234567",
        "email": "dima@gmail.com",
        "group": "KB-261"
    })

    with patch("builtins.input", return_value="Dima"):
        lab2.deleteElement()

    assert len(lab2.list) == 0


def test_updateElement():
    lab2.list.clear()
    lab2.list.append({
        "name": "Dima",
        "phone": "0631234567",
        "email": "dima@gmail.com",
        "group": "KB-261"
    })

    with patch("builtins.input", side_effect=[
        "Dima", "Dmitry", "0991234567",
        "dmitry@gmail.com", "KB-252"
    ]):
        lab2.updateElement()

    assert len(lab2.list) == 1
    assert lab2.list[0]["name"] == "Dmitry"
    assert lab2.list[0]["phone"] == "0991234567"
    assert lab2.list[0]["group"] == "KB-252"
