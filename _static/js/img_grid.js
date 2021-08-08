// アイテムのリストを取得
const items = [...document.querySelectorAll(".item")];
const imgorder = js_vars.id_order;

// ドラッグ開始イベントを定義
const handleDragStart = (e) => {
  e.currentTarget.classList.add("dragging");
  e.dataTransfer.effectAllowed = "move";
  let { id } = e.currentTarget;
  e.dataTransfer.setData("application/json", JSON.stringify({ id }));
};

// ドラッグ終了イベントを定義
const handleDragEnd = (e) => e.currentTarget.classList.remove("dragging");

// アイテムにイベントを登録
for (const item of items) {
  item.addEventListener("dragstart", handleDragStart, false);
  item.addEventListener("dragend", handleDragEnd, false);
}

// 要素が重なった際のイベントを定義
const handleDragEnter = (e) => {
  // 子要素へのドラッグを制限
  if (
    [...e.currentTarget.classList].includes("item")    
    ) {
      e.dataTransfer.dropEffect = "none";
    return;
  };
  e.currentTarget.classList.add("over");
};

// 要素が離れた際のイベントを定義
const handleDragLeave = (e) => e.currentTarget.classList.remove("over");

// 要素が重なっている最中のイベントを定義
const handleDragOver = (e) => {
  // 要素が重なった際のブラウザ既定の処理を変更
  e.preventDefault();

  // 子要素へのドラッグを制限
  if (
    [...e.currentTarget.classList].includes("item") 
    ) {
    e.dataTransfer.dropEffect = "none";
    return;
  };
  // ドロップ効果の設定
  e.dataTransfer.dropEffect = "move";
};

// 要素がドロップされた際のイベントを定義
const handleDrop = (e) => {
  // 要素がドロップされた際のブラウザ既定の処理を変更
  e.preventDefault();
  e.currentTarget.classList.remove("over");
  // ブラウザ外からのファイルドロップを制限
  if (e.dataTransfer.files.length > 0) {
    return;
  };
  // 転送データの取得
  let { id } = JSON.parse(e.dataTransfer.getData("application/json"));
  // ドロップ先に要素を追加する
  e.currentTarget.appendChild(document.getElementById(id));
  let imgid4cat = parseInt(document.getElementById(id).id, 10);
  let true_imgpath = "\"" + "img" + imgorder[imgid4cat] + "_cat" + "\"";
  let catpath = "\"" + "category" + parseInt(e.currentTarget.id, 10) + "\"";
  let catofimg = parseInt(document.getElementById(catpath).children[0].id, 10);
  document.getElementById(true_imgpath).value = catofimg;
};


// ドロップ先のリストを取得
const boxes = [...document.querySelectorAll(".box")];

// ドロップ先にイベントを登録
for (const box of boxes) {
  box.addEventListener("dragenter", handleDragEnter, false);
  box.addEventListener("dragleave", handleDragLeave, false);
  box.addEventListener("dragover", handleDragOver, false);
  box.addEventListener("drop", handleDrop, false);
}