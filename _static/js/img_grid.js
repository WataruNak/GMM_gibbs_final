// アイテムのリストを取得
const items = [...document.querySelectorAll(".item")];
const imgorder = js_vars.id_order;
const imgcatpath_list = js_vars.imgcatpath_list;
const num_rounds = js_vars.num_rounds
let default_name_value = js_vars.default_name_value;
let showed_img_id = js_vars.showed_img_id
let img_category_list = js_vars.img_category_list

let img_cat_list = new Array(num_rounds);
  for (let n=0; n<num_rounds; n++) {
    img_cat_list[n] = document.getElementById(imgcatpath_list[n]);
  };

let box_list = new Array(3);
  for (let m=0; m<3; m++) {
    let boxpath = "box" + m;
    box_list[m] = document.getElementById(boxpath)
  };

let boxchildren_list = new Array(3);
  for (let mc=0; mc<3; mc++) {
    let boxchildrenpath = "box" + mc + "_children";
    boxchildren_list[mc] = document.getElementById(boxchildrenpath);
  };

let movingimg_id;

  window.onload = function() {  
    for (let a=0; a<num_rounds; a++) {
      if (img_category_list[a] == "99") {
        img_cat_list[a].value = "99";
      } else {
        img_cat_list[a].value = img_category_list[a]
      }
    };
    document.getElementById("name_order").value = default_name_value;
    for (let d=0; d<3; d++) {
      if (box_list[d].childElementCount>0) {
        let firstlist = [];
        for (let dd=0; dd<box_list[d].childElementCount; dd++) {
          let firstid = Number(box_list[d].children[dd].id);
          firstlist.push(String(firstid));
        };
        boxchildren_list[d].value = firstlist.join(",");
      } else {
        boxchildren_list[d].value = "999"
      };
    };
  };  


let el = document.getElementById('names');
let sortablename = Sortable.create(el, {
  onChange: function (evt) {
    let sorted_order = sortablename.toArray()
    document.getElementById('name_order').value = sortablename.toArray().join(',');
    for (let j=0; j<3; j++) {
      if (box_list[j].childElementCount>0) {
        let childidlist = [];
        for (let jj=0; jj< box_list[j].childElementCount; jj++) {
          let stimid = Number(box_list[j].children[jj].id);
          img_cat_list[stimid].value = sorted_order[j].substr(-1);
          childidlist.push(String(stimid));
        };
        boxchildren_list[j].value = childidlist.join(",");
      } else {
        boxchildren_list[j].value = "999"
      };
    };
  }
});


// ドラッグ開始イベントを定義
$(".item").draggable({
  revert: "invalid",
  start: function(e, ui) {
    movingimg_id = e.target.id;
  }
})

$(".box").droppable({
  accept: ".item",
  activeclass: "over",
  drop: function(e, ui) {
    document.getElementById(movingimg_id).style = "position: relative"
    e.target.appendChild(document.getElementById(movingimg_id))
    let categoryorder = document.getElementById("name_order").value.split(',');
    img_cat_list[movingimg_id].value = categoryorder[Number(e.target.id.substr(-1))].substr(-1);
    for (let k=0; k<3; k++) {
      if (box_list[k].childElementCount>0) {
        let childidlist2 = [];
        for (let kk=0; kk<box_list[k].childElementCount; kk++) {
          let stimid2 = Number(box_list[k].children[kk].id);
          childidlist2.push(String(stimid2));
        };
        boxchildren_list[k].value = childidlist2.join(",");
      } else {
        boxchildren_list[k].value = "999"
      };
    }
    if (
      document.getElementById(imgcatpath_list[showed_img_id]).value != "99") {
      document.getElementById("button_to_se").style.visibility = "visible"
    }
  }
})