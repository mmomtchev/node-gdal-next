#include "layer_features.hpp"
#include "../gdal_common.hpp"
#include "../gdal_feature.hpp"
#include "../gdal_layer.hpp"

namespace node_gdal {

Nan::Persistent<FunctionTemplate> LayerFeatures::constructor;

void LayerFeatures::Initialize(Local<Object> target) {
  Nan::HandleScope scope;

  Local<FunctionTemplate> lcons = Nan::New<FunctionTemplate>(LayerFeatures::New);
  lcons->InstanceTemplate()->SetInternalFieldCount(1);
  lcons->SetClassName(Nan::New("LayerFeatures").ToLocalChecked());

  Nan::SetPrototypeMethod(lcons, "toString", toString);
  Nan::SetPrototypeMethod(lcons, "count", count);
  Nan::SetPrototypeMethod(lcons, "countAsync", countAsync);
  Nan::SetPrototypeMethod(lcons, "add", add);
  Nan::SetPrototypeMethod(lcons, "addAsync", addAsync);
  Nan::SetPrototypeMethod(lcons, "get", get);
  Nan::SetPrototypeMethod(lcons, "getAsync", getAsync);
  Nan::SetPrototypeMethod(lcons, "set", set);
  Nan::SetPrototypeMethod(lcons, "first", first);
  Nan::SetPrototypeMethod(lcons, "firstAsync", firstAsync);
  Nan::SetPrototypeMethod(lcons, "next", next);
  Nan::SetPrototypeMethod(lcons, "nextAsync", nextAsync);
  Nan::SetPrototypeMethod(lcons, "remove", remove);
  Nan::SetPrototypeMethod(lcons, "removeAsync", removeAsync);

  ATTR_DONT_ENUM(lcons, "layer", layerGetter, READ_ONLY_SETTER);

  Nan::Set(target, Nan::New("LayerFeatures").ToLocalChecked(), Nan::GetFunction(lcons).ToLocalChecked());

  constructor.Reset(lcons);
}

LayerFeatures::LayerFeatures() : Nan::ObjectWrap() {
}

LayerFeatures::~LayerFeatures() {
}

/**
 * An encapsulation of a {{#crossLink "gdal.Layer"}}Layer{{/crossLink}}'s
 * features.
 *
 * @class gdal.LayerFeatures
 */
NAN_METHOD(LayerFeatures::New) {
  Nan::HandleScope scope;

  if (!info.IsConstructCall()) {
    Nan::ThrowError("Cannot call constructor as function, you need to use 'new' keyword");
    return;
  }
  if (info[0]->IsExternal()) {
    Local<External> ext = info[0].As<External>();
    void *ptr = ext->Value();
    LayerFeatures *f = static_cast<LayerFeatures *>(ptr);
    f->Wrap(info.This());
    info.GetReturnValue().Set(info.This());
    return;
  } else {
    Nan::ThrowError("Cannot create LayerFeatures directly");
    return;
  }
}

Local<Value> LayerFeatures::New(Local<Value> layer_obj) {
  Nan::EscapableHandleScope scope;

  LayerFeatures *wrapped = new LayerFeatures();

  v8::Local<v8::Value> ext = Nan::New<External>(wrapped);
  v8::Local<v8::Object> obj =
    Nan::NewInstance(Nan::GetFunction(Nan::New(LayerFeatures::constructor)).ToLocalChecked(), 1, &ext).ToLocalChecked();
  Nan::SetPrivate(obj, Nan::New("parent_").ToLocalChecked(), layer_obj);

  return scope.Escape(obj);
}

NAN_METHOD(LayerFeatures::toString) {
  Nan::HandleScope scope;
  info.GetReturnValue().Set(Nan::New("LayerFeatures").ToLocalChecked());
}

/**
 * Fetch a feature by its identifier.
 *
 * **Important:** The `id` argument is not an index. In most cases it will be
 * zero-based, but in some cases it will not. If iterating, it's best to use the
 * `next()` method.
 *
 * @method get
 * @param {Integer} id The feature ID of the feature to read.
 * @return {gdal.Feature}
 */

/**
 * Fetch a feature by its identifier.
 *
 * **Important:** The `id` argument is not an index. In most cases it will be
 * zero-based, but in some cases it will not. If iterating, it's best to use the
 * `next()` method.
 *
 * @method getAsync
 * @param {Integer} id The feature ID of the feature to read.
 * @param {Callback} callback promisifiable callback
 * @return {gdal.Feature}
 */
GDAL_ASYNCABLE_DEFINE(LayerFeatures::get) {
  Nan::HandleScope scope;

  Local<Object> parent =
    Nan::GetPrivate(info.This(), Nan::New("parent_").ToLocalChecked()).ToLocalChecked().As<Object>();
  Layer *layer = Nan::ObjectWrap::Unwrap<Layer>(parent);
  if (!layer->isAlive()) {
    Nan::ThrowError("Layer object already destroyed");
    return;
  }

  int feature_id;
  NODE_ARG_INT(0, "feature id", feature_id);
  OGRLayer *gdal_layer = layer->get();
  long ds_uid = layer->parent_uid;
  GDAL_ASYNCABLE_PERSIST(parent);
  GDAL_ASYNCABLE_MAIN(OGRFeature *) = [ds_uid, gdal_layer, feature_id]() {
    GDAL_ASYNCABLE_LOCK(ds_uid);
    OGRFeature *feature = gdal_layer->GetFeature(feature_id);
    GDAL_UNLOCK_PARENT;
    return feature;
  };
  GDAL_ASYNCABLE_RVAL(OGRFeature *) = [](OGRFeature *feature, GDAL_ASYNCABLE_OBJS) { return Feature::New(feature); };
  GDAL_ASYNCABLE_EXECUTE(1, OGRFeature *);
}

/**
 * Resets the feature pointer used by `next()` and
 * returns the first feature in the layer.
 *
 * @method first
 * @return {gdal.Feature}
 */

/**
 * Resets the feature pointer used by `next()` and
 * returns the first feature in the layer.
 *
 * @method firstAsync
 * @param {Callback} callback promisifiable callback
 * @return {gdal.Feature}
 */
GDAL_ASYNCABLE_DEFINE(LayerFeatures::first) {
  Nan::HandleScope scope;

  Local<Object> parent =
    Nan::GetPrivate(info.This(), Nan::New("parent_").ToLocalChecked()).ToLocalChecked().As<Object>();
  Layer *layer = Nan::ObjectWrap::Unwrap<Layer>(parent);
  if (!layer->isAlive()) {
    Nan::ThrowError("Layer object already destroyed");
    return;
  }

  OGRLayer *gdal_layer = layer->get();
  long ds_uid = layer->parent_uid;
  GDAL_ASYNCABLE_PERSIST(parent);
  GDAL_ASYNCABLE_MAIN(OGRFeature *) = [ds_uid, gdal_layer]() {
    GDAL_ASYNCABLE_LOCK(ds_uid);
    gdal_layer->ResetReading();
    OGRFeature *feature = gdal_layer->GetNextFeature();
    GDAL_UNLOCK_PARENT;
    return feature;
  };
  GDAL_ASYNCABLE_RVAL(OGRFeature *) = [](OGRFeature *feature, GDAL_ASYNCABLE_OBJS) { return Feature::New(feature); };
  GDAL_ASYNCABLE_EXECUTE(0, OGRFeature *);
}

/**
 * Returns the next feature in the layer. Returns null if no more features.
 *
 * @example
 * ```
 * while (feature = layer.features.next()) { ... }```
 *
 * @method next
 * @return {gdal.Feature}
 */

/**
 * Returns the next feature in the layer. Returns null if no more features.
 *
 * @example
 * ```
 * while (feature = layer.features.next()) { ... }```
 *
 * @method nextAsync
 * @param {Callback} callback promisifiable callback
 * @return {gdal.Feature}
 */
GDAL_ASYNCABLE_DEFINE(LayerFeatures::next) {
  Nan::HandleScope scope;

  Local<Object> parent =
    Nan::GetPrivate(info.This(), Nan::New("parent_").ToLocalChecked()).ToLocalChecked().As<Object>();
  Layer *layer = Nan::ObjectWrap::Unwrap<Layer>(parent);
  if (!layer->isAlive()) {
    Nan::ThrowError("Layer object already destroyed");
    return;
  }

  OGRLayer *gdal_layer = layer->get();
  long ds_uid = layer->parent_uid;
  GDAL_ASYNCABLE_PERSIST(parent);
  GDAL_ASYNCABLE_MAIN(OGRFeature *) = [ds_uid, gdal_layer]() {
    GDAL_ASYNCABLE_LOCK(ds_uid);
    OGRFeature *feature = gdal_layer->GetNextFeature();
    GDAL_UNLOCK_PARENT;
    return feature;
  };
  GDAL_ASYNCABLE_RVAL(OGRFeature *) = [](OGRFeature *feature, GDAL_ASYNCABLE_OBJS) { return Feature::New(feature); };
  GDAL_ASYNCABLE_EXECUTE(0, OGRFeature *);
}

/**
 * Adds a feature to the layer. The feature should be created using the current
 * layer as the definition.
 *
 * @example
 * ```
 * var feature = new gdal.Feature(layer);
 * feature.setGeometry(new gdal.Point(0, 1));
 * feature.fields.set('name', 'somestring');
 * layer.features.add(feature);```
 *
 * @method add
 * @throws Error
 * @param {gdal.Feature} feature
 */

/**
 * Adds a feature to the layer. The feature should be created using the current
 * layer as the definition.
 *
 * @example
 * ```
 * var feature = new gdal.Feature(layer);
 * feature.setGeometry(new gdal.Point(0, 1));
 * feature.fields.set('name', 'somestring');
 * layer.features.add(feature);```
 *
 * @method addAsync
 * @throws Error
 * @param {gdal.Feature} feature
 * @param {Callback} callback promisifiable callback
 */

GDAL_ASYNCABLE_DEFINE(LayerFeatures::add) {
  Nan::HandleScope scope;

  Local<Object> parent =
    Nan::GetPrivate(info.This(), Nan::New("parent_").ToLocalChecked()).ToLocalChecked().As<Object>();
  Layer *layer = Nan::ObjectWrap::Unwrap<Layer>(parent);
  if (!layer->isAlive()) {
    Nan::ThrowError("Layer object already destroyed");
    return;
  }

  Feature *f;
  NODE_ARG_WRAPPED(0, "feature", Feature, f)

  OGRLayer *gdal_layer = layer->get();
  long ds_uid = layer->parent_uid;
  OGRFeature *gdal_f = f->get();
  GDAL_ASYNCABLE_PERSIST(parent);
  GDAL_ASYNCABLE_MAIN(int) = [ds_uid, gdal_layer, gdal_f]() {
    GDAL_ASYNCABLE_LOCK(ds_uid);
    int err = gdal_layer->CreateFeature(gdal_f);
    GDAL_UNLOCK_PARENT;
    if (err != CE_None) throw getOGRErrMsg(err);
    return err;
  };
  GDAL_ASYNCABLE_RVAL(int) = [](int, GDAL_ASYNCABLE_OBJS) { return Nan::Undefined(); };
  GDAL_ASYNCABLE_EXECUTE(1, int);
}

/**
 * Returns the number of features in the layer.
 *
 * @method count
 * @param {Boolean} [force=true]
 * @return {Integer} Number of features in the layer.
 */

/**
 * Returns the number of features in the layer.
 *
 * @method countAsync
 * @param {Boolean} [force=true]
 * @param {Callback} callback promisifiable callback
 * @return {Integer} Number of features in the layer.
 */

GDAL_ASYNCABLE_DEFINE(LayerFeatures::count) {
  Nan::HandleScope scope;

  Local<Object> parent =
    Nan::GetPrivate(info.This(), Nan::New("parent_").ToLocalChecked()).ToLocalChecked().As<Object>();
  Layer *layer = Nan::ObjectWrap::Unwrap<Layer>(parent);
  if (!layer->isAlive()) {
    Nan::ThrowError("Layer object already destroyed");
    return;
  }

  Local<Object> ds;
  if (Dataset::dataset_cache.has(layer->getParent())) { ds = Dataset::dataset_cache.get(layer->getParent()); }
  if (!layer->isAlive()) {
    Nan::ThrowError("Dataset object already destroyed");
    return;
  }

  int force = 1;
  NODE_ARG_BOOL_OPT(0, "force", force);

  OGRLayer *gdal_layer = layer->get();
  GDALDataset *gdal_dataset = layer->getParent();
  long ds_uid = layer->parent_uid;
  GDAL_ASYNCABLE_PERSIST(parent, ds);
  GDAL_ASYNCABLE_MAIN(GIntBig) = [ds_uid, gdal_layer, force, gdal_dataset]() {
    GDAL_ASYNCABLE_LOCK(ds_uid);
    GIntBig count = gdal_layer->GetFeatureCount(force);
    GDAL_UNLOCK_PARENT;
    return count;
  };
  GDAL_ASYNCABLE_RVAL(GIntBig) = [](GIntBig count, GDAL_ASYNCABLE_OBJS) { return Nan::New<Number>(count); };
  GDAL_ASYNCABLE_EXECUTE(1, int);
}

/**
 * Sets a feature in the layer.
 *
 * @method set
 * @throws Error
 * @param {Integer} [id]
 * @param {gdal.Feature} feature
 */
NAN_METHOD(LayerFeatures::set) {
  Nan::HandleScope scope;

  Local<Object> parent =
    Nan::GetPrivate(info.This(), Nan::New("parent_").ToLocalChecked()).ToLocalChecked().As<Object>();
  Layer *layer = Nan::ObjectWrap::Unwrap<Layer>(parent);
  if (!layer->isAlive()) {
    Nan::ThrowError("Layer object already destroyed");
    return;
  }

  int err;
  Feature *f;
  int argc = info.Length();

  if (argc == 1) {
    NODE_ARG_WRAPPED(0, "feature", Feature, f);
  } else if (argc == 2) {
    int i = 0;
    NODE_ARG_INT(0, "feature id", i);
    NODE_ARG_WRAPPED(1, "feature", Feature, f);
    err = f->get()->SetFID(i);
    if (err) {
      Nan::ThrowError("Error setting feature id");
      return;
    }
  } else {
    Nan::ThrowError("Invalid number of arguments");
    return;
  }

  if (!f->isAlive()) {
    Nan::ThrowError("Feature already destroyed");
    return;
  }
  err = layer->get()->SetFeature(f->get());
  if (err) {
    NODE_THROW_OGRERR(err);
    return;
  }
  return;
}

/**
 * Removes a feature from the layer.
 *
 * @method remove
 * @throws Error
 * @param {Integer} id
 */

/**
 * Removes a feature from the layer.
 *
 * @method removeAsync
 * @throws Error
 * @param {Integer} id
 * @param {Callback} callback promisifiable callback
 */

GDAL_ASYNCABLE_DEFINE(LayerFeatures::remove) {
  Nan::HandleScope scope;

  Local<Object> parent =
    Nan::GetPrivate(info.This(), Nan::New("parent_").ToLocalChecked()).ToLocalChecked().As<Object>();
  Layer *layer = Nan::ObjectWrap::Unwrap<Layer>(parent);
  if (!layer->isAlive()) {
    Nan::ThrowError("Layer object already destroyed");
    return;
  }

  int i;
  NODE_ARG_INT(0, "feature id", i);

  OGRLayer *gdal_layer = layer->get();
  long ds_uid = layer->parent_uid;
  GDAL_ASYNCABLE_PERSIST(parent);
  GDAL_ASYNCABLE_MAIN(int) = [ds_uid, gdal_layer, i]() {
    GDAL_ASYNCABLE_LOCK(ds_uid);
    int err = gdal_layer->DeleteFeature(i);
    GDAL_UNLOCK_PARENT;
    if (err) {
      throw getOGRErrMsg(err);
    }
    return err;
  };
  GDAL_ASYNCABLE_RVAL(int) = [](int, GDAL_ASYNCABLE_OBJS) { return Nan::Undefined(); };
  GDAL_ASYNCABLE_EXECUTE(1, int);

  return;
}

/**
 * Parent layer
 *
 * @attribute layer
 * @type {gdal.Layer}
 */
NAN_GETTER(LayerFeatures::layerGetter) {
  Nan::HandleScope scope;
  info.GetReturnValue().Set(Nan::GetPrivate(info.This(), Nan::New("parent_").ToLocalChecked()).ToLocalChecked());
}

} // namespace node_gdal
