#ifndef __NODE_GDAL_MDARRAY_H__
#define __NODE_GDAL_MDARRAY_H__

// node
#include <node.h>
#include <node_object_wrap.h>

// nan
#include "nan-wrapper.h"

// gdal
#include <gdal_priv.h>

// ogr
#include <ogrsf_frmts.h>

#include "async.hpp"

#if GDAL_VERSION_MAJOR > 3 || (GDAL_VERSION_MAJOR == 3 && GDAL_VERSION_MINOR >= 1)

using namespace v8;
using namespace node;

namespace node_gdal {

class MDArray : public Nan::ObjectWrap {
    public:
  static Nan::Persistent<FunctionTemplate> constructor;
  static void Initialize(Local<Object> target);
  static NAN_METHOD(New);
  static Local<Value> New(std::shared_ptr<GDALMDArray> group, GDALDataset *parent_ds);
  GDAL_ASYNCABLE_DECLARE(read);
  static NAN_METHOD(getView);
  static NAN_METHOD(getMask);
  static NAN_METHOD(asDataset);
  static NAN_METHOD(toString);
  static NAN_GETTER(typeGetter);
  static NAN_GETTER(lengthGetter);
  static NAN_GETTER(srsGetter);
  static NAN_GETTER(unitTypeGetter);
  static NAN_GETTER(scaleGetter);
  static NAN_GETTER(offsetGetter);
  static NAN_GETTER(noDataValueGetter);
  static NAN_GETTER(dimensionsGetter);
  static NAN_GETTER(descriptionGetter);
  static NAN_GETTER(attributesGetter);
  static NAN_GETTER(uidGetter);

  MDArray(std::shared_ptr<GDALMDArray> ds);
  inline std::shared_ptr<GDALMDArray> get() {
    return this_;
  }

  void dispose();
  long uid;
  long parent_uid;
  size_t dimensions;

  inline bool isAlive() {
    return this_ && object_store.isAlive(uid);
  }

    private:
  ~MDArray();
  std::shared_ptr<GDALMDArray> this_;
  GDALDataset *parent_ds;
};

} // namespace node_gdal
#endif
#endif
