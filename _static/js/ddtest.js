// アイテムのリストを取得
const items = [...document.querySelectorAll(".item")];

// ドラッグ開始イベントを定義
const handleDragStart = (e) => {
  e.target.classList.add("dragging");

  // ドロップ効果の設定
  e.dataTransfer.effectAllowed = "copy";

  // 転送するデータの設定
  const { id } = e.target;
  console.log(e.target);
  e.dataTransfer.setData("application/json", JSON.stringify({ id }));
};

// ドラッグ終了イベントを定義
const handleDragEnd = (e) => e.target.classList.remove("dragging");

// アイテムにイベントを登録
for (const item of items) {
  item.addEventListener("dragstart", handleDragStart, false);
  item.addEventListener("dragend", handleDragEnd, false);
}

// 要素が重なった際のイベントを定義
const handleDragEnter = (e) => {
  // 子要素へのドラッグを制限
  if ([...e.target.classList].includes("item")) {
    return;
  }

  e.target.classList.add("over");
};

// 要素が離れた際のイベントを定義
const handleDragLeave = (e) => e.target.classList.remove("over");

// 要素が重なっている最中のイベントを定義
const handleDragOver = (e) => {
  // 要素が重なった際のブラウザ既定の処理を変更
  e.preventDefault();

  // 子要素へのドラッグを制限
  if ([...e.target.classList].includes("item")) {
    // ドラッグ不可のドロップ効果を設定
    e.dataTransfer.dropEffect = "none";
    return;
  }

  // ドロップ効果の設定
  e.dataTransfer.dropEffect = "copy";
};

// 要素がドロップされた際のイベントを定義
const handleDrop = (e) => {
  // 要素がドロップされた際のブラウザ既定の処理を変更
  e.preventDefault();
  e.target.classList.remove("over");

  // ブラウザ外からのファイルドロップを制限
  if (e.dataTransfer.files.length > 0) {
    return;
  }

  // 転送データの取得
  const { id } = JSON.parse(e.dataTransfer.getData("application/json"));

  // ドロップ先に要素を追加する
  e.target.appendChild(document.getElementById(id));
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